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
