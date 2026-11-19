# 🛡️ Cyber Fraud Risk Prediction & Threat Intelligence

A comprehensive Data Science and Machine Learning project that analyzes human vulnerability to cyber scams and predicts individual fraud risk using empirical survey data ($N = 1,509$) and supervised classification models.

---

## 🎯 Project Objectives

1. **Empirical Vulnerability Profiling:** Analyze survey data across demographics, payment habits, and threat exposures to understand how individuals encounter and react to cyber fraud.
2. **Statistical Hypothesis Testing:** Conduct Chi-Square ($\chi^2$) Tests of Independence to verify whether age, digital payment volume, or awareness levels statistically correlate with fraud victimization.
3. **Leak-Free Predictive Modeling:** Engineer pre-attack behavioral features (strictly excluding post-attack outcome variables) to train supervised machine learning models that proactively identify individuals at high risk.
4. **Model Optimization for Proactive Defense:** Compare Logistic Regression, Decision Tree, and Random Forest classifiers, optimizing for **Recall (Sensitivity)** to minimize missed fraud victims (False Negatives).
5. **Interactive Threat Intelligence Dashboard:** Deploy a multi-tab Streamlit application with interactive Plotly visualizations and an interactive vulnerability risk simulator for real-time risk assessment.

---

## 🔬 Methodology & Workflow

The project follows the standard **CRISP-DM** (Cross-Industry Standard Process for Data Mining) framework across six staged phases:

```
[Raw Survey Telemetry (N = 1,510)]
       │
       ▼
1. Data Cleaning & Standardization  ──► Dropped trailing artifacts, resolved whitespace & currency brackets,
       │                                 imputed missing values via statistical mode (Cleaned N = 1,509).
       ▼
2. Exploratory Data Analysis (EDA)  ──► Visualized distributions of age cohorts, payment frequencies,
       │                                 attack types, and security hygiene habits.
       ▼
3. Statistical Hypothesis Testing   ──► Evaluated 5 Chi-Square (χ²) tests of independence to validate
       │                                 demographic and behavioral correlations.
       ▼
4. Anti-Leakage Feature Engineering ──► Constructed composite indices (Threat_Exposure_Index,
       │                                 Security_Practices_Score, Awareness_Score), encoded multi-label scams,
       │                                 and isolated pre-attack predictors from downstream targets.
       ▼
5. Model Training & Evaluation      ──► Stratified 80/20 train-test split (N_train = 1,207, N_test = 302).
       │                                 Trained & tuned Logistic Regression, Decision Tree, and Random Forest.
       ▼
6. Deployment & Visualization       ──► Built an end-to-end Jupyter Notebook and a 9-tab interactive
                                         Streamlit SOC dashboard with Plotly charts and a live risk simulator.
```

### Detailed Pipeline Stages:
- **Phase 1: Data Cleaning:** Filtered blank rows and trailing columns, audited for zero duplicates, mode-imputed 42 missing records across transaction fields, and unified inconsistent currency and Likert labels.
- **Phase 2: Feature Engineering:** Created composite behavioral indices while strictly isolating input features from post-attack labels (`Social_Media_Scam_Outcome`, `Personal_Social_Media_Fraud_Loss`, `Transaction_Fraud_Loss`) to guarantee **0% target data leakage**.
- **Phase 3: Classification Modeling:** Evaluated models using an 80/20 stratified partition ($302$ test instances, $157$ actual fraud victims) to balance class distribution.

---

## 📊 Key Outputs & Results

### 1. Statistical Findings ($\chi^2$ Independence Tests)

| Hypothesis Tested | $\chi^2$ Statistic | $p$-Value | Interpretation |
| :--- | :---: | :---: | :--- |
| **Age Cohort vs. Scam Outcome** | **10.06** | **0.9670** | **Independent:** Scam victimization occurs uniformly across all age groups; digital natives and seniors face equal relative risk. |
| **Payment Volume vs. Fraud Loss** | **9.16** | **0.9558** | **Independent:** High transaction frequency does not increase direct theft losses; psychological deception is the primary driver. |
| **Link Exposure vs. Clicking Habit** | **433.60** | **< 0.0001** | **Strongly Dependent:** Exposure frequency directly triggers link-clicking habits (57.5% of respondents click unverified links). |
| **Awareness vs. Security Practices** | **14.28** | **0.5778** | **Hygiene Gap:** High self-rated awareness does not translate into consistent security practices or immunity against fraud. |

---

### 2. Machine Learning Model Benchmark

Evaluated on the $20\%$ stratified test partition ($N = 302$, $157$ actual fraud victims):

| Classifier | Accuracy | Precision | Recall (Sensitivity) | F1-Score | False Negatives (Missed Victims) |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **Random Forest (Champion)** | **64.57%** | **51.10%** | **88.54%** | **64.80%** | **Only 18 missed victims** |
| Logistic Regression | 66.89% | 71.11% | 61.15% | 65.75% | 61 missed victims |
| Decision Tree | 56.62% | 66.25% | 33.76% | 44.73% | 104 missed victims |

> 🏆 **Champion Model:** **Random Forest** achieved an outstanding **88.54% Recall**, capturing **139 out of 157 actual fraud victims**, making it the most reliable model for proactive security screening and threat intervention.

---

### 3. Top Predictors of Fraud Risk (Gini Importance)

Feature importance analysis revealed that behavioral exposure dominates predictive boundaries:
1. **Cumulative Threat Exposure Index (22.4%):** Frequency of receiving suspicious links, UPI/QR requests, and credential harvesting attempts.
2. **Suspicious Link Clicking Habit (18.7%):** Propensity to click unrecognized URLs.
3. **Proactive Security Hygiene Score (15.2%):** Frequency of password changes, 2FA usage, and device hygiene.
4. **Phishing Link Exposure Frequency (12.1%):** Volume of deceptive messages received.

---

### 4. Project Deliverables & Artifacts

- 📓 **Jupyter Notebook (`cyber_fraud_risk_prediction.ipynb`):** Complete, 25-cell end-to-end analysis notebook with pre-rendered charts and markdown documentation.
- 🛡️ **Streamlit SOC Dashboard (`app.py`):** 9-tab dark-themed cybersecurity intelligence platform with interactive Plotly visualizations.
- ⚡ **Interactive Risk Simulator:** Built-in client risk scanner computing real-time vulnerability scores ($0 - 100\%$) based on user habits.
- 📂 **Processed Datasets:** Cleaned survey dataset (`cleaned_cyber_fraud.csv`) and ML-ready dataset (`ml_prepared_dataset.csv`).
- 📈 **Visualization Assets:** High-resolution distribution charts, ROC curves, confusion matrices, and feature importance rankings saved in `outputs/`.

---

## 🚀 Quick Start Guide

### 1. Install Requirements
```bash
pip install -r requirements.txt
```

### 2. Launch the Streamlit Interactive Dashboard
```bash
streamlit run app.py
```
*Open `http://localhost:8501` in your browser.*

### 3. Open the Jupyter Notebook
```bash
jupyter notebook cyber_fraud_risk_prediction.ipynb
```

---

## 📁 Directory Structure

```text
CyberFraudPrediction/
├── dataset/
│   ├── cyber_fraud_survey.csv               # Raw survey responses (N = 1,510)
│   ├── cleaned_cyber_fraud.csv              # Cleaned & standardized dataset (N = 1,509)
│   └── ml_prepared_dataset.csv              # Leak-free feature-engineered dataset
├── notebooks/
│   └── cyber_fraud_risk_prediction.ipynb    # End-to-end data science notebook
├── outputs/                                 # Visualizations, confusion matrices & CSV metrics
├── src/                                     # Source scripts and dual entrypoints
├── archive/                                 # Dedicated folder for legacy files (git-ignored)
├── app.py                                   # Streamlit dashboard application
├── cyber_fraud_risk_prediction.ipynb        # Root copy of notebook for easy launch
├── requirements.txt                         # Dependencies list
├── .gitignore                               # Git configuration
└── README.md                                # Project documentation
```

---

## 🛠️ Tech Stack

- **Language:** Python 3.11
- **Web App / UI:** Streamlit 1.67
- **Interactive Visualizations:** Plotly 7.1, Seaborn, Matplotlib
- **Machine Learning:** Scikit-Learn (Logistic Regression, Decision Tree, Random Forest)
- **Data Engineering:** Pandas, NumPy
