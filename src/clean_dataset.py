"""
Script: clean_dataset.py
Project: Cyber Fraud Risk Prediction and Cybersecurity Awareness Analysis
Description:
    Cleans and standardizes the cyber fraud survey dataset without unnecessary data loss.

Tasks performed:
    1. Removes duplicate records if present.
    2. Drops fully empty rows and uninformative unnamed columns.
    3. Handles missing values appropriately using mode imputation for survey categories.
    4. Standardizes inconsistent labels, whitespace, casing, and currency notations.
    5. Saves the cleaned dataset as 'cleaned_cyber_fraud.csv'.
"""

from pathlib import Path
import re
import pandas as pd


def get_dataset_paths():
    """Resolve input and output paths relative to script or workspace."""
    script_dir = Path(__file__).resolve().parent
    workspace_dir = script_dir.parent

    # Input file candidates
    input_candidates = [
        workspace_dir / "dataset" / "cyber_fraud_survey.csv",
        Path("dataset/cyber_fraud_survey.csv"),
        Path("cyber_fraud_survey.csv"),
    ]
    input_path = None
    for p in input_candidates:
        if p.exists():
            input_path = p
            break
    if input_path is None:
        raise FileNotFoundError("Could not find raw 'cyber_fraud_survey.csv'.")

    # Output paths (save in dataset/ folder and workspace root for convenience)
    output_dataset_path = workspace_dir / "dataset" / "cleaned_cyber_fraud.csv"
    output_root_path = workspace_dir / "cleaned_cyber_fraud.csv"

    return input_path, output_dataset_path, output_root_path


def clean_text(val):
    """Normalize string whitespace and characters."""
    if pd.isna(val):
        return val
    s = str(val).strip()
    s = re.sub(r"\s+", " ", s)  # collapse multiple spaces into one
    return s


def clean_personal_fraud_loss(val):
    """Standardize loss categories for personal social media fraud."""
    if pd.isna(val):
        return val
    s = str(val).strip()
    s_lower = s.lower()

    if s_lower == "no":
        return "No"
    if s_lower == "not sure":
        return "Not sure"
    if "less than" in s_lower:
        return "Less than Rs. 500"
    if "2000" in s_lower or "2,000" in s_lower:
        return "Rs. 2,000 - Rs. 5,000"
    if "50001" in s_lower or ("10000" in s_lower and "more" not in s_lower):
        return "Rs. 5,001 - Rs. 10,000"
    if "more than" in s_lower:
        return "More than Rs. 10,000"
    return s


def clean_transaction_fraud_loss(val):
    """Standardize loss categories for digital payment transaction fraud."""
    if pd.isna(val):
        return val
    s = str(val).strip()
    s_lower = s.lower()

    if s_lower == "no":
        return "No"
    if "less than" in s_lower:
        return "Less than Rs. 500"
    if "500" in s_lower and ("2000" in s_lower or "2,000" in s_lower):
        return "Rs. 500 - Rs. 2,000"
    if "2001" in s_lower or "2,001" in s_lower:
        return "Rs. 2,001 - Rs. 5,000"
    return s


def clean_digital_transactions(val):
    """Standardize transaction frequency categories."""
    if pd.isna(val):
        return val
    s = str(val).strip()
    s_lower = s.lower()

    if s_lower in ["more than 14 times/week", "more than 14 times / week", "more than 30"]:
        return "More than 14 times / week"
    if s_lower in ["1-2 times", "1-3 times / week"]:
        return "1-3 times / week"
    return s


def clean_scam_outcome(val):
    """Standardize scam outcome labels."""
    if pd.isna(val):
        return val
    s = re.sub(r"\s+", " ", str(val).strip())
    if s == "Clicked/contacted but no loss occurred":
        return "Clicked the link but no loss occurred"
    return s


def clean_dataset():
    input_path, output_dataset_path, output_root_path = get_dataset_paths()
    print("=" * 70)
    print("CYBER FRAUD SURVEY DATASET CLEANING PIPELINE")
    print("=" * 70)
    print(f"Reading raw dataset: {input_path}")
    df = pd.read_csv(input_path)
    initial_shape = df.shape
    print(f"Raw shape: {initial_shape[0]} rows, {initial_shape[1]} columns")

    # Step 1: Remove uninformative trailing empty columns (e.g. Unnamed: 16, 17, 18)
    unnamed_cols = [c for c in df.columns if c.startswith("Unnamed:")]
    if unnamed_cols:
        print(f"\nDropping empty trailing columns: {unnamed_cols}")
        df.drop(columns=unnamed_cols, inplace=True)

    # Step 2: Drop completely empty rows (all values are NaN)
    empty_rows_before = df.isnull().all(axis=1).sum()
    if empty_rows_before > 0:
        print(f"Dropping {empty_rows_before} completely blank row(s)...")
        df.dropna(how="all", inplace=True)

    # Step 3: Remove duplicate records if present
    duplicates_count = df.duplicated().sum()
    print(f"\nDuplicate rows check: {duplicates_count} found.")
    if duplicates_count > 0:
        df.drop_duplicates(inplace=True)
        print("Duplicate rows removed.")

    # Step 4: Strip leading/trailing whitespaces across all string columns
    str_cols = df.select_dtypes(include="object").columns
    for col in str_cols:
        df[col] = df[col].apply(clean_text)

    # Step 5: Standardize inconsistent categorical values
    print("\nStandardizing categorical values and inconsistent labels...")

    # Standardize Social_Media_Hours ('More than 5 hours' -> '4-6 hours')
    df["Social_Media_Hours"] = df["Social_Media_Hours"].replace(
        {"More than 5 hours": "4-6 hours"}
    )

    # Standardize Digital_Transactions_Per_Week
    df["Digital_Transactions_Per_Week"] = df["Digital_Transactions_Per_Week"].apply(
        clean_digital_transactions
    )

    # Standardize Social_Media_Scam_Outcome
    df["Social_Media_Scam_Outcome"] = df["Social_Media_Scam_Outcome"].apply(
        clean_scam_outcome
    )

    # Standardize Fraud_Identification_Ability ('5 -  Excellent' -> '5 - Excellent', etc.)
    df["Fraud_Identification_Ability"] = df["Fraud_Identification_Ability"].replace(
        {
            "5 -  Excellent": "5 - Excellent",
            "2 -  Poor": "2 - Poor",
        }
    )

    # Standardize Personal_Social_Media_Fraud_Loss
    df["Personal_Social_Media_Fraud_Loss"] = df[
        "Personal_Social_Media_Fraud_Loss"
    ].apply(clean_personal_fraud_loss)

    # Standardize Transaction_Fraud_Loss
    df["Transaction_Fraud_Loss"] = df["Transaction_Fraud_Loss"].apply(
        clean_transaction_fraud_loss
    )

    # Standardize Name to Title Case
    if "Name" in df.columns:
        df["Name"] = df["Name"].astype(str).str.title().str.strip()

    # Step 6: Handle missing values appropriately (without unnecessary data loss)
    print("\nHandling missing values:")
    missing_before = df.isnull().sum()
    for col, count in missing_before[missing_before > 0].items():
        mode_val = df[col].mode()[0]
        pct = (count / len(df)) * 100
        print(
            f"  - Column '{col}': {count} missing ({pct:.2f}%). Imputing with mode: '{mode_val}'"
        )
        df[col].fillna(mode_val, inplace=True)

    # Step 7: Enforce clean data types
    if "Overall_Cybersecurity_Awareness" in df.columns:
        df["Overall_Cybersecurity_Awareness"] = pd.to_numeric(
            df["Overall_Cybersecurity_Awareness"], errors="coerce"
        ).astype(int)

    # Final Verification
    final_shape = df.shape
    remaining_nulls = df.isnull().sum().sum()
    print("\n" + "=" * 70)
    print("CLEANING COMPLETED SUCCESSFULLY")
    print("=" * 70)
    print(f"Final Cleaned Dataset Shape: {final_shape[0]} rows, {final_shape[1]} columns")
    print(f"Remaining Missing Values:    {remaining_nulls}")
    print(f"Remaining Duplicate Records: {df.duplicated().sum()}")

    # Step 8: Save cleaned dataset
    df.to_csv(output_dataset_path, index=False)
    df.to_csv(output_root_path, index=False)
    print(f"\nSaved cleaned dataset to:")
    print(f"  1. {output_dataset_path}")
    print(f"  2. {output_root_path}")
    print("=" * 70)

    return df


if __name__ == "__main__":
    clean_dataset()
