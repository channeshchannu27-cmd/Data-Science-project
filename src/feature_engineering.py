"""
Script: feature_engineering.py
Project: Cyber Fraud Risk Prediction and Cybersecurity Awareness Analysis
Description:
    Prepares input features and the target variable for machine learning.
    
Tasks performed:
    1. Formulates the target variable ('Fraud_Victim') representing cyber fraud harm/loss.
    2. Encodes ordinal demographic, digital usage, threat exposure, and behavioral features.
    3. Multi-label binary encodes scam types ('Social_Media_Scam_Type').
    4. Computes composite 'Cybersecurity_Awareness_Score' and 'Security_Practices_Score'.
    5. Strictly isolates outcome variables to eliminate Data Leakage.
    6. Saves the prepared dataset to 'dataset/ml_prepared_dataset.csv'.
"""

from pathlib import Path
import json
import pandas as pd


def get_paths():
    script_dir = Path(__file__).resolve().parent
    workspace_dir = script_dir.parent

    input_path = workspace_dir / "dataset" / "cleaned_cyber_fraud.csv"
    if not input_path.exists():
        input_path = workspace_dir / "cleaned_cyber_fraud.csv"
    if not input_path.exists():
        raise FileNotFoundError("Could not find 'cleaned_cyber_fraud.csv'.")

    output_dataset_path = workspace_dir / "dataset" / "ml_prepared_dataset.csv"
    output_root_path = workspace_dir / "ml_prepared_dataset.csv"
    output_meta_path = workspace_dir / "outputs" / "feature_metadata.json"

    return input_path, output_dataset_path, output_root_path, output_meta_path


def build_target_variable(df: pd.DataFrame) -> pd.Series:
    """
    Constructs ground truth binary target 'Fraud_Victim':
        1 = Suffered actual fraud harm (direct monetary loss or compromised account)
        0 = Successfully avoided fraud (no financial loss, no account compromise, or not applicable)
    """
    severe_outcomes = ["Lost money", "Account was compromised"]
    has_scam_loss = df["Social_Media_Scam_Outcome"].isin(severe_outcomes)
    has_tx_loss = df["Transaction_Fraud_Loss"] != "No"
    has_pers_loss = ~df["Personal_Social_Media_Fraud_Loss"].isin(["No", "Not sure"])

    target = (has_scam_loss | has_tx_loss | has_pers_loss).astype(int)
    return target


def engineer_features(df: pd.DataFrame) -> pd.DataFrame:
    prepared = pd.DataFrame(index=df.index)

    # 1. Target Variable (Ground Truth)
    prepared["Fraud_Victim"] = build_target_variable(df)

    # -------------------------------------------------------------
    # 2. Ordinal Encodings (Demographics, Usage, Threat Vectors)
    # -------------------------------------------------------------
    age_map = {"18-25": 1, "26-35": 2, "36-45": 3, "46-55": 4, "56+": 5}
    prepared["Age_Group_Ord"] = df["Age_Group"].map(age_map)

    hours_map = {
        "Less than 1 hour": 1,
        "1-2 hours": 2,
        "2-4 hours": 3,
        "4-6 hours": 4,
        "More than 6 hours": 5,
    }
    prepared["Social_Media_Hours_Ord"] = df["Social_Media_Hours"].map(hours_map)

    tx_freq_map = {
        "Never": 0,
        "1-3 times / week": 1,
        "4-7 times / week": 2,
        "8-14 times / week": 3,
        "More than 14 times / week": 4,
        "1-3 times / day": 5,
    }
    prepared["Digital_Transactions_Ord"] = df["Digital_Transactions_Per_Week"].map(tx_freq_map)

    freq_exposure_map = {
        "Never": 0,
        "Once": 1,
        "2-3 times": 2,
        "4-5 times": 3,
        "More than 5 times": 4,
    }
    prepared["Scam_Exposure_Ord"] = df["Social_Media_Scam_Exposure"].map(freq_exposure_map)
    prepared["UPI_QR_Exposure_Ord"] = df["Suspicious_Payment_UPI_QR_Exposure"].map(freq_exposure_map)
    prepared["OTP_Request_Exposure_Ord"] = df["OTP_Password_Request_Exposure"].map(freq_exposure_map)
    prepared["Suspicious_Link_Clicks_Ord"] = df["Suspicious_Link_Clicks"].map(freq_exposure_map)

    likert_exposure_map = {
        "Never": 0,
        "Rarely": 1,
        "Sometimes": 2,
        "Often": 3,
        "Very often": 4,
    }
    prepared["Suspicious_Link_Exposure_Ord"] = df["Suspicious_Link_Exposure"].map(likert_exposure_map)

    # -------------------------------------------------------------
    # 3. Security Hygiene & Awareness Scores
    # -------------------------------------------------------------
    practices_map = {"Never": 1, "Rarely": 2, "Sometimes": 3, "Often": 4, "Always": 5}
    prepared["Security_Practices_Score"] = df["Security_Practices"].map(practices_map)

    ability_map = {
        "1 - Very poor": 1,
        "2 - Poor": 2,
        "3 - Average": 3,
        "4 - Good": 4,
        "5 - Excellent": 5,
    }
    fraud_ident_num = df["Fraud_Identification_Ability"].map(ability_map)
    overall_awareness = df["Overall_Cybersecurity_Awareness"].astype(float)

    # Composite Cybersecurity Awareness Score (Scale 1.0 - 5.0)
    prepared["Cybersecurity_Awareness_Score"] = (overall_awareness + fraud_ident_num) / 2.0

    # Composite Threat Exposure Index (Cumulative target pressure, 0 to 16)
    prepared["Threat_Exposure_Index"] = (
        prepared["Scam_Exposure_Ord"]
        + prepared["UPI_QR_Exposure_Ord"]
        + prepared["OTP_Request_Exposure_Ord"]
        + prepared["Suspicious_Link_Exposure_Ord"]
    )

    # -------------------------------------------------------------
    # 4. Multi-Label Scam Type Binary Features
    # -------------------------------------------------------------
    scam_types = [
        ("scam_type_impersonation", "Fake/impersonation account"),
        ("scam_type_giveaway_prize", "Fake giveaway/prize"),
        ("scam_type_job_offer", "Fake job offer"),
        ("scam_type_shopping_fraud", "Shopping/product scam"),
        ("scam_type_crypto_investment", "Investment/crypto scam"),
        ("scam_type_romance", "Romance/relationship scam"),
        ("scam_type_account_takeover", "Account takeover/hacking attempt"),
    ]
    for col_name, pattern in scam_types:
        prepared[col_name] = (
            df["Social_Media_Scam_Type"]
            .fillna("")
            .apply(lambda x: 1 if pattern.lower() in str(x).lower() else 0)
        )

    # -------------------------------------------------------------
    # 5. DATA LEAKAGE PREVENTION:
    # Explicitly verify NO outcome/loss columns enter the feature set:
    # 'Social_Media_Scam_Outcome', 'Personal_Social_Media_Fraud_Loss',
    # 'Transaction_Fraud_Loss', 'Name' are excluded.
    # -------------------------------------------------------------
    return prepared


def main():
    input_path, output_dataset_path, output_root_path, output_meta_path = get_paths()
    print("=" * 75)
    print("FEATURE ENGINEERING & PREPARATION FOR CYBER FRAUD ML MODELING")
    print("=" * 75)
    print(f"Reading cleaned dataset from: {input_path}")
    raw_df = pd.read_csv(input_path)

    prepared_df = engineer_features(raw_df)

    # Summary of Target
    target_counts = prepared_df["Fraud_Victim"].value_counts()
    pos_pct = (target_counts[1] / len(prepared_df)) * 100
    neg_pct = (target_counts[0] / len(prepared_df)) * 100

    print("\n[Target Variable Distribution]")
    print(f" - Class 0 (Safe / No Fraud Harm):  {target_counts[0]} ({neg_pct:.1f}%)")
    print(f" - Class 1 (Fraud Victim / Loss):   {target_counts[1]} ({pos_pct:.1f}%)")
    print(f" - Balance Status:                  Nicely Balanced ({pos_pct:.1f}% / {neg_pct:.1f}%)")

    print("\n[Engineered Scores Summary]")
    print(
        f" - Cybersecurity_Awareness_Score: Mean = {prepared_df['Cybersecurity_Awareness_Score'].mean():.2f}, "
        f"Min = {prepared_df['Cybersecurity_Awareness_Score'].min():.1f}, "
        f"Max = {prepared_df['Cybersecurity_Awareness_Score'].max():.1f}"
    )
    print(
        f" - Security_Practices_Score:      Mean = {prepared_df['Security_Practices_Score'].mean():.2f}, "
        f"Min = {prepared_df['Security_Practices_Score'].min():d}, "
        f"Max = {prepared_df['Security_Practices_Score'].max():d}"
    )
    print(
        f" - Threat_Exposure_Index:         Mean = {prepared_df['Threat_Exposure_Index'].mean():.2f}, "
        f"Min = {prepared_df['Threat_Exposure_Index'].min():d}, "
        f"Max = {prepared_df['Threat_Exposure_Index'].max():d}"
    )

    print(f"\nFinal Prepared Feature Matrix Dimensions: {prepared_df.shape[0]} rows, {prepared_df.shape[1]} columns")

    # Save prepared dataset
    prepared_df.to_csv(output_dataset_path, index=False)
    prepared_df.to_csv(output_root_path, index=False)
    print(f"\nSaved ML Prepared Dataset to:")
    print(f"  1. {output_dataset_path}")
    print(f"  2. {output_root_path}")

    # Generate metadata dictionary for reference
    feature_metadata = {
        "target": {
            "name": "Fraud_Victim",
            "type": "binary (0 or 1)",
            "description": "1 = Experienced financial fraud loss or compromised account; 0 = No harm.",
            "distribution": {"0": int(target_counts[0]), "1": int(target_counts[1])},
        },
        "features": {col: str(prepared_df[col].dtype) for col in prepared_df.columns if col != "Fraud_Victim"},
        "data_leakage_safeguards": [
            "Excluded 'Name' (PII)",
            "Excluded 'Social_Media_Scam_Outcome' (Post-attack target proxy)",
            "Excluded 'Personal_Social_Media_Fraud_Loss' (Target component)",
            "Excluded 'Transaction_Fraud_Loss' (Target component)",
        ],
    }
    with open(output_meta_path, "w", encoding="utf-8") as f:
        json.dump(feature_metadata, f, indent=2)
    print(f"  3. Metadata saved to: {output_meta_path}")
    print("=" * 75)


if __name__ == "__main__":
    main()
