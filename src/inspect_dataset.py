"""
Script: inspect_dataset.py
Project: Cyber Fraud Risk Prediction and Cybersecurity Awareness Analysis
Description:
    Inspects and summarizes the cyber fraud survey dataset without modifying it.
    Tasks covered:
    1. Load the dataset using pandas.
    2. Display the number of rows and columns.
    3. Display all column names.
    4. Show the first 5 rows.
    5. Identify data types.
    6. Check missing values and duplicate rows.
    7. Provide a short summary explanation of the dataset.
"""

from pathlib import Path
import pandas as pd


def get_dataset_path() -> Path:
    """Resolve dataset path whether running from root, src, or notebooks folder."""
    candidate_paths = [
        Path("dataset/cyber_fraud_survey.csv"),
        Path("../dataset/cyber_fraud_survey.csv"),
        Path(__file__).resolve().parent.parent / "dataset" / "cyber_fraud_survey.csv",
    ]
    for path in candidate_paths:
        if path.exists():
            return path
    raise FileNotFoundError("Could not locate 'cyber_fraud_survey.csv'.")


def main():
    print("=" * 70)
    print("CYBER FRAUD SURVEY DATASET INITIAL INSPECTION")
    print("=" * 70)

    # 1. Load the dataset using Pandas
    dataset_path = get_dataset_path()
    print(f"\n[Task 1] Loading dataset from: {dataset_path}")
    df = pd.read_csv(dataset_path)
    print("Dataset loaded successfully.")

    # 2. Display the number of rows and columns
    rows, cols = df.shape
    print(f"\n[Task 2] Dataset Shape:")
    print(f" - Rows:    {rows}")
    print(f" - Columns: {cols}")

    # 3. Display all column names
    print(f"\n[Task 3] Column Names ({len(df.columns)} total):")
    for idx, col in enumerate(df.columns, 1):
        print(f"  {idx:2d}. {col}")

    # 4. Show the first 5 rows
    print("\n[Task 4] First 5 Rows of the Dataset:")
    print("-" * 70)
    # Configure pandas display options to ensure readable terminal output
    pd.set_option("display.max_columns", None)
    pd.set_option("display.width", 1000)
    print(df.head())

    # 5. Identify data types
    print("\n[Task 5] Column Data Types:")
    print("-" * 70)
    print(df.dtypes)

    # 6. Check missing values and duplicate rows
    print("\n[Task 6] Missing Values and Duplicates Check:")
    print("-" * 70)
    print("Missing values per column:")
    missing_series = df.isnull().sum()
    for col, count in missing_series.items():
        percentage = (count / rows) * 100
        print(f"  - {col:<38}: {count:4d} missing ({percentage:5.2f}%)")

    duplicate_count = df.duplicated().sum()
    print(f"\nTotal duplicate rows: {duplicate_count}")

    # 7. Short explanation of the dataset
    print("\n" + "=" * 70)
    print("[Task 7] Dataset Summary & Explanation")
    print("=" * 70)
    explanation = """
This dataset contains survey responses regarding cybersecurity awareness,
behavioral patterns, and exposure to various forms of cyber fraud.

Key Feature Categories:
1. Demographics & Usage:
   - Respondent name, age group, social media screen time, and frequency
     of weekly digital transactions.
2. Threat Exposure & Attack Types:
   - Encounters with social media scams (impersonation, crypto scams, job
     offers, fake giveaways), suspicious UPI/QR payment requests, phishing
     links, and deceptive OTP/password requests.
3. Impact & Loss:
   - Financial loss incurred from social media scams and digital transaction
     fraud, alongside user action taken (e.g., ignored, clicked link, lost money).
4. Security Habits & Awareness:
   - Daily cybersecurity practices, self-rated fraud identification ability,
     and overall cybersecurity awareness level.

Dataset Observations for Future Steps:
- The raw file contains 1,510 rows and 19 columns (including 3 unnamed empty
  trailing columns from trailing commas, and a blank first row).
- High completeness across core survey questions with no duplicate response rows.
"""
    print(explanation.strip())
    print("=" * 70)


if __name__ == "__main__":
    main()
