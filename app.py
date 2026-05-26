from flask import Flask, render_template, request, redirect, url_for, flash, send_file
import pandas as pd
import joblib
import os
import uuid

app = Flask(__name__)
app.secret_key = "your_secret_key"  # Needed for flash messages

# Ensure uploads folder exists
UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Load model and scaler using correct filenames
model = joblib.load("models/log_reg_fraud.pkl")
scaler = joblib.load("models/amount_scaler.pkl")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/predict_csv", methods=["POST"])
def predict_csv():
    if "file" not in request.files:
        flash("No file part in the request.")
        return redirect(url_for("index"))

    file = request.files["file"]
    if file.filename == "":
        flash("No file selected.")
        return redirect(url_for("index"))

    # Validate file type
    if not file.filename.lower().endswith(".csv"):
        flash("Only CSV files are allowed.")
        return redirect(url_for("index"))

    # Save uploaded file to uploads folder
    filepath = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(filepath)

    try:
        # Read and preprocess
        data = pd.read_csv(filepath)

        if data.empty:
            flash("Uploaded CSV is empty.")
            return redirect(url_for("index"))

        if "Time" in data.columns:
            data = data.drop("Time", axis=1)

        if "Amount" in data.columns:
            data["Amount"] = scaler.transform(data[["Amount"]])

        X = data.drop("Class", axis=1, errors="ignore")
        predictions = model.predict(X)

        # Add predictions to dataframe
        data["Prediction"] = predictions

        fraud_count = int((predictions == 1).sum())
        total = int(len(predictions))
        fraud_ratio = round((fraud_count / total) * 100, 2) if total > 0 else 0

        # Save results to a uniquely named CSV
        result_filename = f"results_{uuid.uuid4().hex[:8]}.csv"
        result_path = os.path.join(UPLOAD_FOLDER, result_filename)
        data.to_csv(result_path, index=False)

        return render_template(
            "result.html",
            total=total,
            fraud_count=fraud_count,
            fraud_ratio=fraud_ratio,
            download_link=url_for("download_results", filename=result_filename)
        )

    except Exception as e:
        flash(f"Error processing file: {str(e)}")
        return redirect(url_for("index"))

@app.route("/download_results/<filename>")
def download_results(filename):
    """Allow users to download the prediction results as CSV."""
    result_path = os.path.join(UPLOAD_FOLDER, filename)
    if os.path.exists(result_path):
        return send_file(result_path, as_attachment=True)
    else:
        flash("No results available to download.")
        return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True)