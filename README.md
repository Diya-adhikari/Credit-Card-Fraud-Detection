# 💳 Credit Card Fraud Detection Web Application
Fraud detection for credit card transactions using Logistic Regression, with a complete workflow including data preprocessing, model training, evaluation, reporting, and a Flask-based web interface.

# 🛡️ Credit Card Fraud Detection

## 📌 Project Overview
This project demonstrates **credit card fraud detection** using **Logistic Regression** integrated into a **Flask web application**.  
The workflow includes: data cleaning, preprocessing, model training, evaluation, saving reports, and building a user-friendly web interface (`index.html` + `result.html` + `styles.css`).

---

## 📂 Repository Contents
- `frauddetection.ipynb` → Complete workflow notebook (data loading → preprocessing → model → evaluation → saving outputs).  
- `app.py` → Flask application for uploading CSVs and running predictions.  
- `requirements.txt` → Python dependencies.  
- `models/` → Saved ML model (`log_reg_fraud.pkl`) and scaler (`amount_scaler.pkl`).  
- `reports/` → Evaluation metrics (`metrics.txt`).  
- `static/` → CSS styles (`styles.css`) and banner image (`fraud_banner.jpg`).  
- `templates/` → HTML templates (`index.html`, `result.html`).  
- `uploads/` → Dataset (`creditcard.csv`) and generated prediction results (`results_xxxxx.csv`).  

---

## ⚙️ Workflow & Steps Completed

### 1. 📑 Data Loading & Exploration
- **Dataset used**: Kaggle Credit Card Fraud Detection dataset.  
- **Shape**: 284,807 rows × 31 columns.  
- **Target**: `Class` (0 = legitimate, 1 = fraud).  
- **Imbalance**: 492 fraud cases vs 284,315 legitimate transactions.  

### 2. 🔄 Data Preprocessing
- Dropped `Time` column.  
- Scaled `Amount` column using `StandardScaler`.  
- Stratified train-test split (80/20).  

### 3. 🤖 Model Training
- **Algorithm**: Logistic Regression.  
- **Parameters**:  
  - `max_iter=500`  
  - `class_weight='balanced'`  
  - `random_state=42`  
- Model trained on preprocessed dataset.  
- Outputs:  
  - Saved model (`log_reg_fraud.pkl`).  
  - Saved scaler (`amount_scaler.pkl`).  

### 4. 📊 Evaluation

**Logistic Regression Fraud Detection Report**

- **Accuracy**: 0.9746  
- **ROC-AUC**: 0.9714  

**Classification Report:**
| Class | Precision | Recall | F1-score | Support |
|-------|-----------|--------|----------|---------|
| 0 (Legitimate) | 1.00 | 0.97 | 0.99 | 56,864 |
| 1 (Fraud)      | 0.06 | 0.92 | 0.11 | 98 |

- **Accuracy (overall)**: 0.97 (56,962 samples)  
- **Macro Average**: Precision 0.53, Recall 0.95, F1-score 0.55  
- **Weighted Average**: Precision 1.00, Recall 0.97, F1-score 0.99  

**Confusion Matrix:**
<img width="1506" height="1402" alt="Screenshot 2026-07-20 212855" src="https://github.com/user-attachments/assets/7e78842a-40b0-4afe-b34f-d8f987d81c5b" />
<img width="1196" height="898" alt="image" src="https://github.com/user-attachments/assets/626c7b0d-4e24-469b-8334-0ae1ac9466fc" />


**Interpretation:**
- The model correctly identified **90 out of 98 fraud cases** (high recall).  
- Precision for fraud is low (0.06), meaning many false positives.  
- This trade-off is common in fraud detection: catching fraud is prioritized over precision.  

---

## 📈 Reports
- `reports/metrics.txt` contains:  
  - Accuracy: 0.9746  
  - ROC-AUC: 0.9714  
  - Classification report (precision, recall, F1-score).  
  - Confusion matrix.

Logistic Regression Fraud Detection Report
Accuracy: 0.9746
ROC-AUC: 0.9714

Classification Report:
              precision    recall  f1-score   support

           0       1.00      0.97      0.99     56864
           1       0.06      0.92      0.11        98

    accuracy                           0.97     56962
   macro avg       0.53      0.95      0.55     56962
weighted avg       1.00      0.97      0.99     56962

Confusion Matrix:
[[55423  1441]
 [    8    90]]

---

## 🎨 Web Interface

### `index.html`
- Navigation bar with links (Home, Upload, About).  
- Hero section with fraud awareness banner and CTA button.  
- Upload section: CSV upload form, spinner animation.  
- Info section: *How it works* (Upload → Preprocess → Results).  
- Features section: Fast Predictions, Secure Processing, Accurate Results.  
- Footer: *Powered by Machine Learning | Built by Diya*.  

### `result.html`
- Displays prediction summary.  
- Results overview: total transactions, fraud count.  
- Fraud ratio progress bar (animated).  
- Banner image.  
- Back to Home + Download Results buttons.  

### `styles.css`
- Purple gradient theme with responsive design.  
- Styled navbar, hero section, cards, buttons.  
- Animations: fade-in, zoom-in, spinner, progress bar.  
- Mobile-friendly layout.  

---

## 📊 Visual Outputs
- **Confusion Matrix Heatmap** → Shows predicted vs actual fraud cases.  
- **ROC Curve** → AUC = 0.9714, strong discriminatory power.  
- **Web UI Screenshots**:  
  - Homepage (upload form).  
  - Results dashboard (fraud ratio, summary, download option).  

---

## 🚀 Key Learnings
- Logistic Regression achieved high recall (92%) for fraud detection, prioritizing catching fraud cases.  
- Precision was low, reflecting false positives — a common trade-off in fraud detection.  
- ROC-AUC score (0.97) confirms strong overall model performance.  
- Integrating ML with Flask provides a practical, user-friendly fraud detection tool.  

---

## 📜 Dataset
- Source: Kaggle Credit Card Fraud Detection dataset.  
- Contains anonymized transaction features (`V1–V28`), `Amount`, `Time`, and `Class`.  

---

## 🏷️ How to Run
1. Install dependencies:  
   ```bash
   pip install -r requirements.txt



