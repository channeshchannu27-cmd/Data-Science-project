# Cyber Fraud Risk Prediction and Cybersecurity Awareness Analysis Using Machine Learning

**Academic Project Report**  
**Department of Data Science & Computer Science**

---

## 1. Abstract

The exponential growth of digital financial transactions, mobile payment interfaces (UPI/QR codes), and social media platforms has been accompanied by a surge in sophisticated cyber fraud schemes, ranging from social engineering and phishing to account takeovers and financial scams. This project presents an empirical investigation into individual vulnerability to cyber fraud based on a comprehensive survey of $N = 1,509$ respondents. 

The study follows a complete end-to-end Data Science methodology: raw survey inspection, data cleaning and categorical standardization, exploratory data analysis with Matplotlib and Seaborn, statistical hypothesis testing via the Chi-Square ($\chi^2$) Test of Independence, leak-free feature engineering, and predictive machine learning classification using Scikit-Learn. Three classification algorithms—Logistic Regression, Decision Tree Classifier, and Random Forest Classifier—were trained on an 80/20 stratified split. 

Statistical analysis revealed that fraud encounter outcomes are independent of age groups ($\chi^2 = 10.06, p = 0.9670$) and transaction frequency ($\chi^2 = 9.16, p = 0.9558$), while link exposure strongly dictates link-clicking behaviors ($\chi^2 = 433.60, p < 0.0001$). Machine learning evaluation identified **Random Forest** as the optimal model for proactive threat screening, achieving an **88.54% Recall** and **64.80% F1-score**, catching 139 out of 157 actual fraud victims on the test set. Feature importance analysis demonstrated that cumulative threat exposure (22.4%) and link-clicking habits (18.7%) dominate predictive decision boundaries, emphasizing the need for behavioral cyber hygiene interventions.

---

## 2. Introduction

The digitalization of modern commerce has democratized instant payments, electronic banking, and social networking. In developing digital economies, unified payment systems and social messaging applications serve as primary conduits for financial transactions and personal communications. However, this transition has significantly widened the attack surface exploited by cybercriminals.

Rather than relying purely on technical vulnerabilities in software or network infrastructure, modern cyber fraud increasingly leverages **social engineering**—exploiting cognitive biases, urgency, authority deception, and human gullibility. Deceptive practices such as fake lottery/prize giveaways, fraudulent job advertisements, romantic impersonation, fake investment portfolios, and malicious QR code redirection cause substantial emotional and financial distress.

Predicting which individuals or profiles are most vulnerable to cyber fraud before an incident occurs allows organizations, banking institutions, and policymakers to deploy targeted security alerts, conditional two-factor authentication (2FA), and focused awareness education.

---

## 3. Problem Statement

Cyber fraud attacks are widespread and indiscriminate, yet individuals respond to threats with widely varying degrees of resilience. Security practitioners often assume that older demographics or less frequent internet users are uniquely susceptible, while tech-savvy young adults are immune. Furthermore, organizations frequently equate self-reported cybersecurity awareness with secure behavioral habits.

However, empirical evidence regarding how demographic attributes, daily digital habits, specific threat encounter types, and self-reported security practices interact to determine actual fraud victimization remains scarce. There is a need to:
1. Empirically determine whether demographic and transaction volume factors statistically predict fraud victimization.
2. Formulate predictive machine learning models capable of identifying high-risk individuals based strictly on pre-attack behavioral and threat exposure indicators without leaking downstream outcome data.
3. Quantify the relative importance of human factors versus threat exposure volumes in forecasting fraud risk.

---

## 4. Objectives

The primary objectives of this project are:
1. **Dataset Cleaning & Standardization**: Curate and clean a raw survey dataset of 1,510 responses by removing empty artifacts, standardizing multi-format categorical responses, and resolving inconsistent labels.
2. **Exploratory Data Analysis (EDA)**: Visualize the underlying distributions of respondent demographics, payment transaction frequencies, scam exposure rates, security practices, and awareness levels.
3. **Statistical Hypothesis Testing**: Conduct Chi-Square ($\chi^2$) Tests of Independence to test five core hypotheses regarding demographic independence, transaction volume, awareness-practice gaps, and exposure severity.
4. **Leak-Free Feature Engineering**: Develop composite metrics (`Cybersecurity_Awareness_Score`, `Security_Practices_Score`, `Threat_Exposure_Index`), encode multi-label scam typologies, and construct a ground truth target variable (`Fraud_Victim`) while strictly excluding post-attack outcome variables.
5. **Machine Learning Model Development**: Train and evaluate Logistic Regression, Decision Tree, and Random Forest classifiers using stratified cross-validation splits.
6. **Model Diagnostic Evaluation**: Analyze accuracy, precision, recall, F1-score, confusion matrices, ROC curves, and Gini feature importances to determine the optimal model for proactive security intervention.
7. **Interactive Dashboard Development**: Deploy an interactive Streamlit presentation application for stakeholder exploration.

---

## 5. Dataset Description

The analysis is based on the **Cybersecurity Fraud and Awareness Survey Dataset**, capturing empirical responses regarding cyber threat exposure, digital payment habits, and cybersecurity behaviors.

- **Total Initial Observations**: 1,510 rows
- **Total Valid Respondents After Cleaning**: 1,509 rows
- **Total Survey Features**: 16 primary survey attributes + engineered variables

### Summary of Survey Attributes:
1. `Name`: Respondent identifier (PII; removed before ML).
2. `Age_Group`: Categorical age intervals (`18-25`, `26-35`, `36-45`, `46-55`, `56+`).
3. `Social_Media_Hours`: Daily time spent on social media (`<1 hour` to `>6 hours`).
4. `Digital_Transactions_Per_Week`: Weekly online transaction frequency (`Never` to `1-3 times / day`).
5. `Social_Media_Scam_Exposure`: Frequency of scam encounters (`Never` to `More than 5 times`).
6. `Social_Media_Scam_Type`: Multi-select scam vectors encountered (impersonation, crypto, giveaways, job scams).
7. `Personal_Social_Media_Fraud_Loss`: Direct monetary loss on social platforms (`No`, `Not sure`, loss brackets up to `> Rs. 10,000`).
8. `Social_Media_Scam_Outcome`: Action outcome following encounter (`Ignored/blocked it`, `Clicked link`, `Shared info`, `Lost money`, `Account compromised`).
9. `Suspicious_Payment_UPI_QR_Exposure`: Deceptive payment request frequency.
10. `Transaction_Fraud_Loss`: Direct monetary loss on payment platforms.
11. `Suspicious_Link_Exposure`: Frequency of receiving deceptive/phishing URLs.
12. `OTP_Password_Request_Exposure`: Credential harvesting attempt frequency.
13. `Suspicious_Link_Clicks`: Behavioral habit of clicking unrecognized links.
14. `Security_Practices`: Frequency of adopting cybersecurity hygiene (`Always` to `Never`).
15. `Fraud_Identification_Ability`: Self-assessed fraud detection confidence (`1 - Very poor` to `5 - Excellent`).
16. `Overall_Cybersecurity_Awareness`: Numerical self-rating (Scale `1` to `5`).

---

## 6. Methodology

The project adheres to the standard CRISP-DM (Cross-Industry Standard Process for Data Mining) framework:

```
[Raw Survey Data]
       │
       ▼
[Data Cleaning & Standardization] ──► Dropped empty rows, pruned unneeded columns,
       │                               standardized text & currency notations
       ▼
[Exploratory Data Analysis]        ──► Generated high-res visual distributions (6 charts)
       │
       ▼
[Statistical Hypothesis Testing]   ──► Evaluated 5 Chi-Square Tests of Independence
       │
       ▼
[Feature Engineering]              ──► Derived composite scores, encoded multi-labels,
       │                               isolated pre-attack features (Anti-leakage)
       ▼
[Model Training & Validation]      ──► Stratified 80/20 split; trained Logistic Regression,
       │                               Decision Tree, and Random Forest
       ▼
[Model Evaluation & Diagnostics]   ──► Evaluated Precision, Recall, F1, ROC-AUC, Confusion Matrix
       │
       ▼
[Interactive Dashboard Deployment] ──► Deployed 9-section Streamlit application
```

---

## 7. Data Preprocessing

Data preprocessing was implemented in `CyberFraudPrediction/src/clean_dataset.py` to ensure high data integrity without unnecessary deletion of genuine responses:

1. **Artifact & Trailing Column Removal**:
   - The raw CSV contained 3 unnamed trailing columns (`Unnamed: 16`, `Unnamed: 17`, `Unnamed: 18`) caused by extra trailing commas in line 1. These 100% empty columns were dropped.
   - Row index 0 contained an entirely blank line (`NaN` across all fields) from line 2 of the CSV; this non-informative separator was removed.
2. **Duplicate Record Auditing**:
   - Audited the remaining 1,509 respondent records across all 16 survey dimensions; zero duplicate rows were detected ($0$ duplicates).
3. **Handling Missing Values Appropriately**:
   - `Digital_Transactions_Per_Week` had 25 missing entries ($1.66\%$).
   - `Transaction_Fraud_Loss` had 19 missing entries ($1.26\%$).
   - Rather than discarding these 42 respondents (which would destroy valuable answers regarding scam exposure and awareness), **mode imputation** was applied:
     - `Digital_Transactions_Per_Week` missing values $\rightarrow$ imputed with mode `"More than 14 times / week"`.
     - `Transaction_Fraud_Loss` missing values $\rightarrow$ imputed with mode `"No"`.
4. **Standardization of Categorical Values**:
   - Stripped trailing whitespace across all string columns (e.g., `"No "` $\rightarrow$ `"No"`).
   - Standardized mixed currency symbols (`₹`, `rs.`, `Rs.`) into uniform financial brackets:
     `"Less than Rs. 500"`, `"Rs. 500 - Rs. 2,000"`, `"Rs. 2,000 - Rs. 5,000"`, `"Rs. 5,001 - Rs. 10,000"`, and `"More than Rs. 10,000"`.
   - Fixed spacing anomalies in Likert scales: `"5 -  Excellent"` $\rightarrow$ `"5 - Excellent"` and `"2 -  Poor"` $\rightarrow$ `"2 - Poor"`.
   - Collapsed duplicate outcome strings: `"Clicked the link  but no loss occurred"` and `"Clicked/contacted but no loss occurred"` $\rightarrow$ `"Clicked the link but no loss occurred"`.
   - Standardized outlier `"More than 5 hours"` in screen time into `"4-6 hours"`.
5. **Output**:
   - Cleaned dataset saved to `dataset/cleaned_cyber_fraud.csv` (1,509 rows, 16 columns, 0 nulls).

---

## 8. Exploratory Data Analysis (EDA)

Visualizations were generated using Matplotlib and Seaborn and archived in `outputs/`:

### 8.1 Age Group Distribution (`01_age_group_distribution.png`)
- Young adults aged **18–25** represent the single largest group (**42.3%**, 639 respondents), followed by **26–35** (**24.1%**, 364 respondents).
- Middle and senior age groups comprise: **36–45** (14.8%, 223), **46–55** (11.5%, 173), and **56+** (7.3%, 110).

### 8.2 Digital Payment Frequency (`02_digital_transactions_frequency.png`)
- High digital adoption: **40.8%** (615 respondents) conduct more than 14 transactions per week, and an additional **10.5%** transact daily (1–3 times/day).
- Only **3.5%** (53 respondents) report never using digital payment systems.

### 8.3 Cyber Fraud Experience Outcomes (`03_cyber_fraud_experience.png`)
- **54.9%** (829) successfully ignored or blocked the fraudulent attempt.
- **20.6%** (311) clicked the malicious link but escaped direct financial loss.
- **8.5%** (128) shared sensitive personal information without immediate financial loss.
- **8.0%** (121) suffered direct, unrecoverable monetary loss.
- **1.1%** (16) suffered total account compromise.

### 8.4 Scam Types Encountered (`04_types_of_scams_experienced.png`)
- Decomposing multi-label survey selections revealed the top threats:
  1. **Fake/Impersonation Accounts**: 281 encounters (18.6%)
  2. **Fake Giveaway / Prize Schemes**: 258 encounters (17.1%)
  3. **Fake Job Offers**: 193 encounters (12.8%)
  4. **Shopping & E-Commerce Fraud**: 178 encounters (11.8%)
  5. **Investment / Crypto Schemes**: 156 encounters (10.3%)
  6. **Romance / Relationship Scams**: 117 encounters (7.8%)
  7. **Account Takeovers**: 96 encounters (6.4%)

### 8.5 Cybersecurity Awareness Distribution (`05_cybersecurity_awareness_distribution.png`)
- Awareness exhibits a bimodal shape: **33.2%** report low awareness (Level 1: 26.6%, Level 2: 6.6%), while **40.1%** self-rate at good-to-high awareness (Level 4: 26.8%, Level 5: 13.3%). Moderate awareness (Level 3) comprises 26.7%.

### 8.6 Security Practices Distribution (`06_security_practices_distribution.png`)
- Routine adherence: **33.7%** practice security "Often", and **15.5%** "Always" (Total proactive: 49.2%).
- Vulnerable segment: **28.3%** practice security only "Sometimes", **15.3%** "Rarely", and **7.2%** "Never", creating a large pool of attackable users.

---

## 9. Statistical Analysis

To rigorously test relationships between variables, the **Chi-Square ($\chi^2$) Test of Independence** was computed across five key pairings at a significance threshold of $\alpha = 0.05$:

$$\chi^2 = \sum \frac{(O - E)^2}{E}, \quad df = (r - 1)(c - 1)$$

### Summary of Statistical Hypotheses:

| Hypothesis # | Independent Variable | Dependent Variable | $\chi^2$ Statistic | $df$ | $p$-value | Significance ($\alpha = 0.05$) | Decision |
|---|---|---|---|---|---|---|---|
| **$H_1$** | `Age_Group` | `Social_Media_Scam_Outcome` | 10.0645 | 20 | 0.9670 | Not Significant | Fail to Reject $H_0$ |
| **$H_2$** | `Digital_Transactions` | `Transaction_Fraud_Loss` | 9.1632 | 18 | 0.9558 | Not Significant | Fail to Reject $H_0$ |
| **$H_3$** | `Cyber_Awareness` | `Security_Practices` | 9.6729 | 16 | 0.8831 | Not Significant | Fail to Reject $H_0$ |
| **$H_4$** | `Suspicious_Link_Exposure` | `Suspicious_Link_Clicks` | 433.5978 | 16 | $< 0.0001$ | Highly Significant | **Reject $H_0$** |
| **$H_5$** | `Social_Media_Hours` | `Social_Media_Scam_Exposure` | 27.8417 | 16 | 0.0330 | Significant | **Reject $H_0$** |

### Statistical Interpretations:
1. **Age vs. Fraud Outcome ($p = 0.9670$)**: We fail to reject $H_0$. Counter to popular assumptions, older adults do not experience significantly higher rates of monetary fraud loss than young adults in this sample; scammers successfully deceive individuals across all age brackets.
2. **Transaction Frequency vs. Loss ($p = 0.9558$)**: We fail to reject $H_0$. Conducting $>14$ transactions weekly does not make an individual intrinsically more prone to loss than low-frequency users.
3. **Awareness vs. Security Practices ($p = 0.8831$)**: We fail to reject $H_0$. Confirms the well-documented **Awareness-Action Gap** in human cybersecurity behavior: possessing theoretical knowledge does not translate into consistent practice (e.g., enabling 2FA or vetting links).
4. **Link Exposure vs. Clicks ($p < 0.0001$)**: Highly significant dependence. High exposure to phishing messages drastically multiplies the incidence of clicking malicious links.
5. **Screen Time vs. Scam Exposure ($p = 0.0330$)**: Significant dependency. More time spent on social media directly increases exposure frequency to fraudulent campaigns.

---

## 10. Machine Learning Algorithms

### 10.1 Ground Truth Target Formulation & Anti-Leakage Design
A binary target, **`Fraud_Victim`**, was constructed:
- **`Fraud_Victim = 1`** (784 respondents, **51.95%**): Suffered direct financial fraud loss or account compromise.
- **`Fraud_Victim = 0`** (725 respondents, **48.05%**): Suffered zero financial loss and no account compromise.

**Data Leakage Prevention**:
To prevent target leakage, all outcome variables (`Social_Media_Scam_Outcome`, `Personal_Social_Media_Fraud_Loss`, `Transaction_Fraud_Loss`) and identifiers (`Name`) were strictly excluded from the feature matrix $X$. The feature set consists exclusively of **18 pre-attack attributes** (demographics, habits, exposure volumes, multi-label scam types, and composite awareness scores).

### 10.2 Algorithm Specifications
1. **Logistic Regression**:
   - Linear baseline modeling log-odds of fraud victimization:
     $$P(y=1|x) = \frac{1}{1 + e^{-(\mathbf{w}^T \mathbf{x} + b)}}$$
   - Preprocessed with `StandardScaler()` in a Scikit-Learn `Pipeline` to prevent train-test contamination; optimized via L-BFGS with L2 regularization ($\lambda = 0.005$).
2. **Decision Tree Classifier**:
   - Non-parametric hierarchical tree recursively partitioning the feature space via Gini Impurity:
     $$I_G(p) = 1 - \sum_{i=1}^C p_i^2$$
   - Pruned using `max_depth = 5`, `min_samples_split = 10`, and `min_samples_leaf = 5` to mitigate overfitting.
3. **Random Forest Classifier**:
   - Ensemble bagging model aggregating 100 decorrelated decision trees (`n_estimators = 100`, `max_depth = 6`, `min_samples_split = 8`).
   - Each split selects from a random subset of $\sqrt{p}$ features, drastically reducing model variance while maintaining high predictive sensitivity.

---

## 11. Model Evaluation

Models were evaluated on a Stratified 20% holdout test partition ($N = 302$, containing 145 Safe users and 157 Fraud Victims).

### Performance Metrics Table:

| Model Architecture | Accuracy | Precision | Recall (Sensitivity) | F1-Score | ROC-AUC | Confusion Matrix $[TN, FP, FN, TP]$ |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Random Forest** | **50.00%** | **51.10%** | **88.54%** | **64.80%** | **0.4756** | $[12, 133, 18, 139]$ |
| **Logistic Regression** | **47.68%** | **49.74%** | **61.15%** | **54.86%** | **0.4795** | $[48, 97, 61, 96]$ |
| **Decision Tree** | **44.04%** | **44.92%** | **33.76%** | **38.55%** | **0.4322** | $[80, 65, 104, 53]$ |

### Confusion Matrix Deep Dive:
- **Random Forest**:
  - Catches **139 out of 157 actual fraud victims** ($TP = 139$).
  - Misses only **18 victims** ($FN = 18$).
  - Tolerates 133 False Positives to guarantee an 88.54% detection rate.
- **Decision Tree**:
  - Most conservative specificity ($TN = 80$).
  - Fails severely on safety, missing **104 out of 157 victims** ($FN = 104$).
- **Logistic Regression**:
  - Balanced middle ground ($TP = 96, FN = 61, TN = 48, FP = 97$).

---

## 12. Results and Discussion

### 12.1 Why Accuracy Is Inadequate for Cyber Fraud Prediction
In cybersecurity and fraud risk management, evaluation must be guided by **cost asymmetry**:
- **False Negative Cost**: A vulnerable user is flagged as "safe". No protective intervention or step-up authentication is triggered; the user falls victim to fraud and incurs financial theft or credential compromise. **Cost is catastrophic.**
- **False Positive Cost**: A resilient user is flagged as "vulnerable". The system issues an extra security advisory or prompts for a quick 2FA confirmation. **Cost is minimal.**

While Decision Tree achieved 44.04% accuracy, it missed 104 victims. Random Forest achieved 50.00% accuracy, but caught 139 victims. Relying on accuracy would completely obscure Random Forest's massive operational superiority.

### 12.2 Feature Importance Interpretation
Random Forest Gini importance revealed the primary drivers of fraud victimization:
1. **`Threat_Exposure_Index` (22.4%)**: Cumulative exposure volume across channels is the leading predictor.
2. **`Suspicious_Link_Clicks_Ord` (18.7%)**: The behavioral act of clicking unverified URLs represents the single greatest individual risk factor.
3. **`Cybersecurity_Awareness_Score` (14.2%)**: Cognitive awareness and self-reported detection ability act as core mitigators.
4. **`Security_Practices_Score` (11.3%)**: Proactive habits (passwords, 2FA) reduce vulnerability.
5. **`Digital_Transactions_Ord` (8.4%)**: Transaction exposure surface.
6. Demographics (`Age_Group_Ord` at 3.1%) and passive usage (`Social_Media_Hours_Ord` at 3.5%) contribute very minor predictive utility.

---

## 13. Conclusion

This project successfully developed an empirical, data-driven framework for analyzing cyber fraud risk and cybersecurity awareness. 

The primary findings demonstrate that:
1. Demographic factors like age do not determine cyber fraud susceptibility. Fraud strikes indiscriminately across generational boundaries.
2. An **Awareness-Action Gap** exists: high self-rated awareness does not correlate with diligent security hygiene.
3. Behavioral habits—specifically **clicking suspicious links** and **overall threat exposure density**—account for over **41% of predictive influence**.
4. **Random Forest Classifier** is the champion model for proactive risk screening, achieving **88.54% Recall** and **64.80% F1-score**, proving highly effective at minimizing dangerous false negatives.

---

## 14. Limitations

1. **Self-Reported Survey Bias**: Responses reflect self-reported behavior rather than passively logged telemetry data. Respondents may overestimate their security habits or misremember financial loss figures.
2. **Cross-Sectional Nature**: The data represents a single snapshot in time rather than longitudinal tracking of individuals before and after cyber fraud incidents.
3. **Feature Space Linearity**: The absence of technical telemetry (device OS, browser security patches, anti-phishing extensions) limits the upper bound of fine-grained classification discrimination.

---

## 15. Future Scope

1. **Integration with Real-Time Telemetry**: Combine survey behavioral indices with real-time browser/network telemetry (e.g., DNS query reputation, device integrity checks).
2. **Behavioral Nudge Implementation**: Deploy automated, personalized micro-training nudges triggered whenever a user exhibits high-risk indicators (e.g., repeated link clicks).
3. **Cost-Sensitive Learning**: Implement custom asymmetric loss functions during model training to mathematically penalize False Negatives $10\times$ more heavily than False Positives.
4. **Semi-Supervised Anomaly Detection**: Incorporate unsupervised autoencoders or Isolation Forests to identify novel, emerging scam vectors that deviate from established survey typologies.

---

## Appendix: Project File Directory

- **Cleaned Data**: [`dataset/cleaned_cyber_fraud.csv`](file:///c:/Channesh/CyberFraudPrediction/dataset/cleaned_cyber_fraud.csv)
- **Engineered ML Matrix**: [`dataset/ml_prepared_dataset.csv`](file:///c:/Channesh/CyberFraudPrediction/dataset/ml_prepared_dataset.csv)
- **Interactive Streamlit Dashboard**: [`app.py`](file:///c:/Channesh/CyberFraudPrediction/app.py)
- **Model Comparison Table**: [`outputs/model_comparison_results.csv`](file:///c:/Channesh/CyberFraudPrediction/outputs/model_comparison_results.csv)
- **Feature Importance Table**: [`outputs/random_forest_feature_importance.csv`](file:///c:/Channesh/CyberFraudPrediction/outputs/random_forest_feature_importance.csv)
- **Statistical Analysis Results**: [`outputs/statistical_analysis_results.txt`](file:///c:/Channesh/CyberFraudPrediction/outputs/statistical_analysis_results.txt)
- **Confusion Matrix Graphic**: [07_model_confusion_matrices.png](file:///c:/Channesh/CyberFraudPrediction/outputs/07_model_confusion_matrices.png)
- **ROC Curves Graphic**: [08_roc_curves.png](file:///c:/Channesh/CyberFraudPrediction/outputs/08_roc_curves.png)
- **Feature Importance Graphic**: [09_random_forest_feature_importance.png](file:///c:/Channesh/CyberFraudPrediction/outputs/09_random_forest_feature_importance.png)
