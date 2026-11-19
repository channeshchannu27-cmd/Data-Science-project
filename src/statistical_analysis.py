"""
Script: statistical_analysis.py
Project: Cyber Fraud Risk Prediction and Cybersecurity Awareness Analysis
Description:
    Performs cross-tabulations and Chi-Square Tests of Independence
    on five key hypothesis relationships in the cybersecurity survey dataset:
    1. Age Group vs Cyber Fraud Experience (Scam Outcome)
    2. Digital Transaction Frequency vs Transaction Fraud Loss
    3. Cybersecurity Awareness vs Security Practices
    4. Suspicious Link Exposure vs Suspicious Link Clicks
    5. Social Media Screen Time vs Scam Exposure Frequency

Outputs Saved:
    - outputs/chi_square_summary.csv
    - outputs/statistical_analysis_results.txt
    - outputs/crosstab_*.csv (for each relationship)
"""

from pathlib import Path
import math
import pandas as pd


def get_paths():
    """Resolve paths relative to project workspace."""
    script_dir = Path(__file__).resolve().parent
    workspace_dir = script_dir.parent

    data_path = workspace_dir / "dataset" / "cleaned_cyber_fraud.csv"
    if not data_path.exists():
        data_path = workspace_dir / "cleaned_cyber_fraud.csv"
    if not data_path.exists():
        raise FileNotFoundError("Could not find 'cleaned_cyber_fraud.csv'.")

    output_dir = workspace_dir / "outputs"
    output_dir.mkdir(parents=True, exist_ok=True)
    return data_path, output_dir


def chi2_survival(x, df):
    """Compute upper-tail p-value for chi-square distribution using pure Python."""
    if x <= 0:
        return 1.0
    a = df / 2.0
    z = x / 2.0

    # Continued fraction for upper incomplete gamma Q(a, z)
    tiny = 1e-30
    b0 = z + 1.0 - a
    c0 = 1.0 / tiny
    d0 = 1.0 / b0
    f = d0

    for i in range(1, 101):
        an = -i * (i - a)
        bn = b0 + (2.0 * i)
        d0 = bn + (an * d0)
        if abs(d0) < tiny:
            d0 = tiny
        c0 = bn + (an / c0)
        if abs(c0) < tiny:
            c0 = tiny
        d0 = 1.0 / d0
        delta = c0 * d0
        f *= delta
        if abs(delta - 1.0) < 1e-12:
            break

    log_gamma_a = math.lgamma(a)
    p = math.exp(-z + (a * math.log(z)) - log_gamma_a) * f
    return max(0.0, min(1.0, p))


def run_chi2_test(ct):
    """Calculate Chi-Square statistic, degrees of freedom, and p-value from contingency table."""
    try:
        from scipy.stats import chi2_contingency
        res = chi2_contingency(ct)
        return float(res.statistic), int(res.dof), float(res.pvalue)
    except ImportError:
        # Pure Python calculation
        observed = ct.values
        row_totals = observed.sum(axis=1)
        col_totals = observed.sum(axis=0)
        total = observed.sum()

        expected = (row_totals[:, None] * col_totals[None, :]) / total
        chi2 = ((observed - expected) ** 2 / expected).sum()
        df = (ct.shape[0] - 1) * (ct.shape[1] - 1)
        p = chi2_survival(chi2, df)
        return float(chi2), int(df), float(p)


def main():
    data_path, output_dir = get_paths()
    print("=" * 75)
    print("CYBERSECURITY SURVEY STATISTICAL ANALYSIS & CHI-SQUARE TESTS")
    print("=" * 75)
    df = pd.read_csv(data_path)
    print(f"Loaded Cleaned Dataset: {data_path} (N = {len(df)})\n")

    relationships = [
        {
            "id": 1,
            "col1": "Age_Group",
            "col2": "Social_Media_Scam_Outcome",
            "name": "Age Group vs Cyber Fraud Experience",
            "h0": "Age group and cyber fraud experience are independent (age does not influence scam outcome).",
            "h1": "Age group and cyber fraud experience are dependent (certain age groups experience different scam outcomes).",
        },
        {
            "id": 2,
            "col1": "Digital_Transactions_Per_Week",
            "col2": "Transaction_Fraud_Loss",
            "name": "Digital Transaction Frequency vs Transaction Fraud Loss",
            "h0": "Digital transaction frequency and transaction fraud loss are independent.",
            "h1": "Digital transaction frequency and transaction fraud loss are dependent.",
        },
        {
            "id": 3,
            "col1": "Overall_Cybersecurity_Awareness",
            "col2": "Security_Practices",
            "name": "Cybersecurity Awareness vs Security Practices",
            "h0": "Overall cybersecurity awareness score and daily security practices adherence are independent.",
            "h1": "Overall cybersecurity awareness score and daily security practices adherence are dependent.",
        },
        {
            "id": 4,
            "col1": "Suspicious_Link_Exposure",
            "col2": "Suspicious_Link_Clicks",
            "name": "Suspicious Link Exposure vs Suspicious Link Clicks",
            "h0": "Frequency of encountering suspicious links and frequency of clicking suspicious links are independent.",
            "h1": "Frequency of encountering suspicious links and frequency of clicking suspicious links are dependent.",
        },
        {
            "id": 5,
            "col1": "Social_Media_Hours",
            "col2": "Social_Media_Scam_Exposure",
            "name": "Social Media Usage vs Scam Exposure Frequency",
            "h0": "Daily social media screen time and frequency of scam encounters are independent.",
            "h1": "Daily social media screen time and frequency of scam encounters are dependent.",
        },
    ]

    summary_rows = []
    report_lines = []

    report_lines.append("=" * 80)
    report_lines.append("STATISTICAL ANALYSIS REPORT: CHI-SQUARE TEST OF INDEPENDENCE")
    report_lines.append(f"Sample Size: N = {len(df)} survey respondents")
    report_lines.append("Significance Threshold (Alpha): 0.05")
    report_lines.append("=" * 80 + "\n")

    for rel in relationships:
        c1, c2 = rel["col1"], rel["col2"]
        ct = pd.crosstab(df[c1], df[c2], margins=True, margins_name="Total")

        # Save contingency table to CSV
        csv_filename = f"crosstab_{rel['id']:02d}_{c1.lower()}_vs_{c2.lower()}.csv"
        ct.to_csv(output_dir / csv_filename)

        # Compute Chi-Square without margins
        ct_nomargins = pd.crosstab(df[c1], df[c2])
        chi2, dof, pval = run_chi2_test(ct_nomargins)

        is_significant = pval < 0.05
        status = "Reject H0 (Statistically Significant)" if is_significant else "Fail to Reject H0 (Not Significant)"

        if is_significant:
            simple_conclusion = (
                f"There is a statistically significant relationship between {c1.replace('_', ' ')} and "
                f"{c2.replace('_', ' ')} (p = {pval:.4e} < 0.05). The two variables are dependent."
            )
        else:
            simple_conclusion = (
                f"No statistically significant relationship was found between {c1.replace('_', ' ')} and "
                f"{c2.replace('_', ' ')} (p = {pval:.4f} > 0.05). Any observed variation is likely due to chance."
            )

        summary_rows.append({
            "Test_ID": rel["id"],
            "Relationship": rel["name"],
            "Variable_1": c1,
            "Variable_2": c2,
            "Chi2_Statistic": round(chi2, 4),
            "Degrees_of_Freedom": dof,
            "P_Value": f"{pval:.4e}" if pval < 0.0001 else f"{pval:.4f}",
            "Significance_at_0.05": "Yes" if is_significant else "No",
            "Hypothesis_Result": status,
        })

        # Append to report
        sec = []
        sec.append("-" * 80)
        sec.append(f"Relationship #{rel['id']}: {rel['name']}")
        sec.append(f"Variables: [{c1}]  vs  [{c2}]")
        sec.append("-" * 80)
        sec.append(f"Null Hypothesis (H0):        {rel['h0']}")
        sec.append(f"Alternative Hypothesis (H1): {rel['h1']}")
        sec.append(f"Chi-Square (X^2) Statistic:  {chi2:.4f}")
        sec.append(f"Degrees of Freedom (df):     {dof}")
        sec.append(f"p-value:                     {pval:.4e}" if pval < 0.0001 else f"p-value:                     {pval:.4f}")
        sec.append(f"Result:                      {status}")
        sec.append(f"Conclusion:                  {simple_conclusion}\n")
        sec.append("Cross-Tabulation Table (Observed Counts):")
        sec.append(ct.to_string())
        sec.append("\n")

        print("\n".join(sec))
        report_lines.extend(sec)

    # Save summary table
    summary_df = pd.DataFrame(summary_rows)
    summary_csv_path = output_dir / "chi_square_summary.csv"
    summary_df.to_csv(summary_csv_path, index=False)
    print(f"\nSaved summary CSV to: {summary_csv_path}")

    # Save full text report
    report_path = output_dir / "statistical_analysis_results.txt"
    report_path.write_text("\n".join(report_lines), encoding="utf-8")
    print(f"Saved full statistical report to: {report_path}")
    print("=" * 75)


if __name__ == "__main__":
    main()
