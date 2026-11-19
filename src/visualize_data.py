"""
Script: visualize_data.py
Project: Cyber Fraud Risk Prediction and Cybersecurity Awareness Analysis
Description:
    Generates high-resolution visualizations for exploratory data analysis
    using Matplotlib and Seaborn based on the cleaned dataset.

Charts Generated:
    1. Age Group Distribution (Bar Chart)
    2. Digital Transaction Frequency (Horizontal Bar Chart)
    3. Cyber Fraud Experience & Outcomes (Horizontal Bar Chart)
    4. Types of Scams Experienced (Horizontal Bar Chart)
    5. Overall Cybersecurity Awareness Level (Bar Chart)
    6. Daily Security Practices Distribution (Bar Chart)
    7. Multi-panel Dashboard Summary (Combined Chart)

Output Directory:
    CyberFraudPrediction/outputs/
"""

from pathlib import Path
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd


def get_paths():
    """Resolve input and output paths."""
    script_dir = Path(__file__).resolve().parent
    workspace_dir = script_dir.parent

    # Candidate paths for cleaned dataset
    candidates = [
        workspace_dir / "dataset" / "cleaned_cyber_fraud.csv",
        workspace_dir / "cleaned_cyber_fraud.csv",
        Path("dataset/cleaned_cyber_fraud.csv"),
        Path("cleaned_cyber_fraud.csv"),
    ]
    data_path = None
    for p in candidates:
        if p.exists():
            data_path = p
            break
    if data_path is None:
        raise FileNotFoundError("Could not find 'cleaned_cyber_fraud.csv'.")

    output_dir = workspace_dir / "outputs"
    output_dir.mkdir(parents=True, exist_ok=True)
    return data_path, output_dir


def set_plotting_style():
    """Configure modern, publication-quality aesthetic."""
    sns.set_theme(style="whitegrid", font="sans-serif")
    plt.rcParams["font.sans-serif"] = ["Segoe UI", "DejaVu Sans", "Helvetica", "Arial"]
    plt.rcParams["axes.edgecolor"] = "#CCCCCC"
    plt.rcParams["axes.linewidth"] = 0.8
    plt.rcParams["grid.color"] = "#EBEBEB"
    plt.rcParams["grid.linestyle"] = "--"
    plt.rcParams["grid.alpha"] = 0.7


def add_bar_labels_vertical(ax, total_count, format_str="{:d}\n({:.1f}%)"):
    """Annotate vertical bars with count and percentage."""
    for p in ax.patches:
        height = p.get_height()
        if height > 0:
            pct = (height / total_count) * 100
            ax.annotate(
                format_str.format(int(height), pct),
                (p.get_x() + p.get_width() / 2.0, height),
                ha="center",
                va="bottom",
                fontsize=9.5,
                fontweight="bold",
                color="#222222",
                xytext=(0, 4),
                textcoords="offset points",
            )


def add_bar_labels_horizontal(ax, total_count, format_str="{:d} ({:.1f}%)"):
    """Annotate horizontal bars with count and percentage."""
    for p in ax.patches:
        width = p.get_width()
        if width > 0:
            pct = (width / total_count) * 100
            ax.annotate(
                format_str.format(int(width), pct),
                (width, p.get_y() + p.get_height() / 2.0),
                ha="left",
                va="center",
                fontsize=9.5,
                fontweight="bold",
                color="#222222",
                xytext=(6, 0),
                textcoords="offset points",
            )


def plot_age_distribution(df, output_dir):
    """Chart 1: Age Group Distribution."""
    fig, ax = plt.subplots(figsize=(8, 5.5), dpi=300)
    order = ["18-25", "26-35", "36-45", "46-55", "56+"]
    counts = df["Age_Group"].value_counts().reindex(order)

    palette = sns.color_palette("Blues_r", n_colors=len(order))
    sns.barplot(x=counts.index, y=counts.values, ax=ax, palette=palette, edgecolor="#333333", linewidth=0.7)

    ax.set_title("Age Group Distribution of Survey Respondents", fontsize=13, fontweight="bold", pad=15)
    ax.set_xlabel("Age Group", fontsize=11, fontweight="bold")
    ax.set_ylabel("Number of Respondents", fontsize=11, fontweight="bold")
    ax.set_ylim(0, max(counts.values) * 1.18)

    add_bar_labels_vertical(ax, len(df))
    plt.tight_layout()
    out_file = output_dir / "01_age_group_distribution.png"
    plt.savefig(out_file, bbox_inches="tight")
    plt.close()
    print(f"Saved: {out_file.name}")


def plot_transaction_frequency(df, output_dir):
    """Chart 2: Digital Transaction Frequency."""
    fig, ax = plt.subplots(figsize=(9, 5.5), dpi=300)
    order = [
        "More than 14 times / week",
        "4-7 times / week",
        "1-3 times / week",
        "8-14 times / week",
        "1-3 times / day",
        "Never",
    ]
    counts = df["Digital_Transactions_Per_Week"].value_counts().reindex(order).fillna(0)

    palette = sns.color_palette("crest_r", n_colors=len(order))
    sns.barplot(x=counts.values, y=counts.index, ax=ax, palette=palette, edgecolor="#333333", linewidth=0.7)

    ax.set_title("Weekly Digital Payment Transaction Frequency", fontsize=13, fontweight="bold", pad=15)
    ax.set_xlabel("Number of Respondents", fontsize=11, fontweight="bold")
    ax.set_ylabel("Transaction Frequency", fontsize=11, fontweight="bold")
    ax.set_xlim(0, max(counts.values) * 1.22)

    add_bar_labels_horizontal(ax, len(df))
    plt.tight_layout()
    out_file = output_dir / "02_digital_transactions_frequency.png"
    plt.savefig(out_file, bbox_inches="tight")
    plt.close()
    print(f"Saved: {out_file.name}")


def plot_fraud_experience(df, output_dir):
    """Chart 3: Cyber Fraud Experience / Scam Outcomes."""
    fig, ax = plt.subplots(figsize=(9.5, 6), dpi=300)
    counts = df["Social_Media_Scam_Outcome"].value_counts()

    # Custom semantic colors: green for safe/ignored, orange for info loss, red for money loss/compromised
    color_map = {
        "Ignored/blocked it": "#2b8a3e",
        "Clicked the link but no loss occurred": "#4dabf7",
        "Shared information but no financial loss": "#f59f00",
        "Lost money": "#e03131",
        "Not applicable": "#868e96",
        "Account was compromised": "#c92a2a",
    }
    colors = [color_map.get(k, "#4dabf7") for k in counts.index]

    sns.barplot(x=counts.values, y=counts.index, ax=ax, palette=colors, edgecolor="#333333", linewidth=0.7)

    ax.set_title("Cyber Fraud Experience: Encounter Outcomes & Impact", fontsize=13, fontweight="bold", pad=15)
    ax.set_xlabel("Number of Respondents", fontsize=11, fontweight="bold")
    ax.set_ylabel("Encounter Outcome", fontsize=11, fontweight="bold")
    ax.set_xlim(0, max(counts.values) * 1.22)

    add_bar_labels_horizontal(ax, len(df))
    plt.tight_layout()
    out_file = output_dir / "03_cyber_fraud_experience.png"
    plt.savefig(out_file, bbox_inches="tight")
    plt.close()
    print(f"Saved: {out_file.name}")


def plot_scam_types(df, output_dir):
    """Chart 4: Types of Scams Experienced (individual categories)."""
    fig, ax = plt.subplots(figsize=(10, 6.5), dpi=300)

    # Split multi-label entries separated by semicolon
    all_scams = []
    for entry in df["Social_Media_Scam_Type"].dropna():
        for item in str(entry).split(";"):
            item_clean = item.strip()
            if item_clean:
                all_scams.append(item_clean)

    scam_series = pd.Series(all_scams).value_counts()

    palette = sns.color_palette("flare_r", n_colors=len(scam_series))
    sns.barplot(x=scam_series.values, y=scam_series.index, ax=ax, palette=palette, edgecolor="#333333", linewidth=0.7)

    ax.set_title("Distribution of Encountered Cyber Scam Types", fontsize=13, fontweight="bold", pad=15)
    ax.set_xlabel("Total Encounter Count", fontsize=11, fontweight="bold")
    ax.set_ylabel("Scam Category", fontsize=11, fontweight="bold")
    ax.set_xlim(0, max(scam_series.values) * 1.25)

    add_bar_labels_horizontal(ax, len(df))
    plt.tight_layout()
    out_file = output_dir / "04_types_of_scams_experienced.png"
    plt.savefig(out_file, bbox_inches="tight")
    plt.close()
    print(f"Saved: {out_file.name}")


def plot_awareness_distribution(df, output_dir):
    """Chart 5: Overall Cybersecurity Awareness Level."""
    fig, ax = plt.subplots(figsize=(8, 5.5), dpi=300)
    order = [1, 2, 3, 4, 5]
    counts = df["Overall_Cybersecurity_Awareness"].value_counts().reindex(order).fillna(0)

    # Gradient from low awareness (light) to high awareness (deep teal)
    palette = ["#ffc9c9", "#ff922b", "#ffd43b", "#74c0fc", "#20c997"]
    labels = ["1 (Very Low)", "2 (Low)", "3 (Moderate)", "4 (Good)", "5 (High)"]

    sns.barplot(x=labels, y=counts.values, ax=ax, palette=palette, edgecolor="#333333", linewidth=0.7)

    ax.set_title("Overall Cybersecurity Awareness Score Distribution (1-5)", fontsize=13, fontweight="bold", pad=15)
    ax.set_xlabel("Awareness Rating Level", fontsize=11, fontweight="bold")
    ax.set_ylabel("Number of Respondents", fontsize=11, fontweight="bold")
    ax.set_ylim(0, max(counts.values) * 1.18)

    add_bar_labels_vertical(ax, len(df))
    plt.tight_layout()
    out_file = output_dir / "05_cybersecurity_awareness_distribution.png"
    plt.savefig(out_file, bbox_inches="tight")
    plt.close()
    print(f"Saved: {out_file.name}")


def plot_security_practices(df, output_dir):
    """Chart 6: Daily Security Practices Adherence."""
    fig, ax = plt.subplots(figsize=(8.5, 5.5), dpi=300)
    order = ["Always", "Often", "Sometimes", "Rarely", "Never"]
    counts = df["Security_Practices"].value_counts().reindex(order).fillna(0)

    # Semantic palette: green for proactive habits, orange/red for poor habits
    palette = ["#2f9e44", "#38d9a9", "#ffe066", "#ffa94d", "#fa5252"]

    sns.barplot(x=counts.index, y=counts.values, ax=ax, palette=palette, edgecolor="#333333", linewidth=0.7)

    ax.set_title("Adherence to Proactive Cybersecurity Practices", fontsize=13, fontweight="bold", pad=15)
    ax.set_xlabel("Frequency of Security Practice Implementation", fontsize=11, fontweight="bold")
    ax.set_ylabel("Number of Respondents", fontsize=11, fontweight="bold")
    ax.set_ylim(0, max(counts.values) * 1.18)

    add_bar_labels_vertical(ax, len(df))
    plt.tight_layout()
    out_file = output_dir / "06_security_practices_distribution.png"
    plt.savefig(out_file, bbox_inches="tight")
    plt.close()
    print(f"Saved: {out_file.name}")


def generate_all_visualizations():
    data_path, output_dir = get_paths()
    print("=" * 70)
    print("GENERATING VISUALIZATIONS FOR CYBER FRAUD SURVEY DATASET")
    print("=" * 70)
    print(f"Loading cleaned dataset: {data_path}")
    df = pd.read_csv(data_path)
    print(f"Dataset shape: {df.shape[0]} rows, {df.shape[1]} columns\n")

    set_plotting_style()

    plot_age_distribution(df, output_dir)
    plot_transaction_frequency(df, output_dir)
    plot_fraud_experience(df, output_dir)
    plot_scam_types(df, output_dir)
    plot_awareness_distribution(df, output_dir)
    plot_security_practices(df, output_dir)

    print("\n" + "=" * 70)
    print("ALL VISUALIZATIONS SUCCESSFULLY GENERATED & SAVED")
    print(f"Destination: {output_dir}")
    print("=" * 70)


if __name__ == "__main__":
    generate_all_visualizations()
