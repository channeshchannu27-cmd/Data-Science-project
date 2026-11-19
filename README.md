# Cyber Fraud Risk Prediction and Cybersecurity Awareness Analysis

A complete Data Science and Machine Learning project analyzing human vulnerability factors, scam exposure, behavioral habits, and predictive fraud risk from survey responses ($N = 1,509$).

---

## Project Structure

```text
CyberFraudPrediction/
│
├── dataset/
│   ├── cyber_fraud_survey.csv               # Raw survey dataset
│   ├── cleaned_cyber_fraud.csv              # Cleaned & standardized dataset
│   └── ml_prepared_dataset.csv              # Feature-engineered dataset ready for ML
│
├── src/
│   ├── inspect_dataset.py                   # Step 1: Initial dataset inspection
│   ├── clean_dataset.py                     # Step 2: Data cleaning & standardization
│   ├── visualize_data.py                    # Step 3: Matplotlib & Seaborn visualizations
│   ├── statistical_analysis.py              # Step 4: Cross-tabulations & Chi-Square tests
│   ├── feature_engineering.py               # Step 5: Encoding, composite scores, leakage prevention
│   ├── train_models.py                      # Step 6: Scikit-learn model training & evaluation
│   └── app.py                               # Step 7: Streamlit interactive presentation dashboard
│
├── outputs/
│   ├── 01_age_group_distribution.png
│   ├── 02_digital_transactions_frequency.png
│   ├── 03_cyber_fraud_experience.png
│   ├── 04_types_of_scams_experienced.png
│   ├── 05_cybersecurity_awareness_distribution.png
│   ├── 06_security_practices_distribution.png
│   ├── 07_model_confusion_matrices.png
│   ├── 08_roc_curves.png
│   ├── 09_random_forest_feature_importance.png
│   ├── chi_square_summary.csv
│   ├── model_comparison_results.csv
│   ├── random_forest_feature_importance.csv
│   ├── feature_metadata.json
│   ├── statistical_analysis_results.txt
│   └── model_evaluation_report.txt
│
├── app.py                                   # Root Streamlit dashboard entrypoint
├── requirements.txt                         # Python dependencies
└── README.md                                # Project documentation
```

---

## How to Run the Project

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Run Pipeline Steps (Optional)
```bash
python src/inspect_dataset.py
python src/clean_dataset.py
python src/visualize_data.py
python src/statistical_analysis.py
python src/feature_engineering.py
python src/train_models.py
```

### 3. Launch the Streamlit Interactive Dashboard
```bash
streamlit run app.py
```

---

## Interactive Dashboard Sections

1. **Dataset Overview**: Key KPI cards, interactive table viewer, schema inspection.
2. **Cyber Fraud Statistics**: Financial loss distributions and scam encounter outcomes.
3. **Age Group Analysis**: Demographic vulnerability breakdown and cross-tabulations.
4. **Digital Payment Behavior**: Transaction volume vs. financial loss categories.
5. **Scam Types**: Multi-label breakdown of 7 distinct scam typologies.
6. **Cybersecurity Awareness**: Self-rated awareness vs. fraud identification ability.
7. **Security Practices**: Hygiene adherence frequency vs. link-clicking rates.
8. **Machine Learning Models**: Side-by-side performance comparison, confusion matrices, and ROC curves.
9. **Feature Importance**: Gini importance rankings from Random Forest and an interactive fraud vulnerability score simulator.
