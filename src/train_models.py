"""
Script: train_models.py
Project: Cyber Fraud Risk Prediction and Cybersecurity Awareness Analysis
Description:
    Trains and evaluates three Scikit-Learn classification models to predict cyber fraud risk:
    1. Logistic Regression (with StandardScaler pipeline)
    2. Decision Tree Classifier (pruned with max_depth to prevent overfitting)
    3. Random Forest Classifier (ensemble of 100 decision trees)

Key Steps:
    - Loads pre-engineered features from 'dataset/ml_prepared_dataset.csv'.
    - Performs an 80/20 Stratified Train-Test Split (seed = 42).
    - Applies feature scaling via Pipeline for Logistic Regression.
    - Trains all three models on the training partition.
    - Evaluates on the unseen test set: Accuracy, Precision, Recall, F1-Score, Confusion Matrix.
    - Outputs a side-by-side comparison table and saves report & confusion matrix plot.
"""

from pathlib import Path
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    confusion_matrix,
    classification_report,
)


def get_paths():
    """Locate dataset and output directories."""
    script_dir = Path(__file__).resolve().parent
    workspace_dir = script_dir.parent

    data_path = workspace_dir / "dataset" / "ml_prepared_dataset.csv"
    if not data_path.exists():
        data_path = workspace_dir / "ml_prepared_dataset.csv"
    if not data_path.exists():
        raise FileNotFoundError("Could not find 'ml_prepared_dataset.csv'.")

    output_dir = workspace_dir / "outputs"
    output_dir.mkdir(parents=True, exist_ok=True)
    return data_path, output_dir


def load_and_split_data(data_path: Path):
    """
    Loads dataset, isolates target, and performs stratified 80/20 train/test split.
    Stratification ensures both splits have the exact same ~52% / 48% class ratio.
    """
    df = pd.read_csv(data_path)
    X = df.drop(columns=["Fraud_Victim"])
    y = df["Fraud_Victim"].astype(int)

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.20, random_state=42, stratify=y
    )

    print(f"Total Observations:    {len(df)}")
    print(f"Training Set (80%):    {len(X_train)} samples")
    print(f"Testing Set (20%):     {len(X_test)} samples")
    print(f"Train Target Ratio:    Class 1 = {(y_train.mean()*100):.1f}%, Class 0 = {((1-y_train.mean())*100):.1f}%")
    print(f"Test Target Ratio:     Class 1 = {(y_test.mean()*100):.1f}%, Class 0 = {((1-y_test.mean())*100):.1f}%\n")

    return X_train, X_test, y_train, y_test, X.columns.tolist()


def build_models():
    """
    Initializes the three classifiers with appropriate hyperparameters and preprocessing.
    """
    models = {
        "Logistic Regression": Pipeline([
            ("scaler", StandardScaler()),
            ("classifier", LogisticRegression(max_iter=1000, random_state=42, solver="lbfgs")),
        ]),
        "Decision Tree": DecisionTreeClassifier(
            max_depth=5,
            min_samples_split=10,
            min_samples_leaf=5,
            random_state=42,
        ),
        "Random Forest": RandomForestClassifier(
            n_estimators=100,
            max_depth=6,
            min_samples_split=8,
            min_samples_leaf=4,
            random_state=42,
            n_jobs=-1,
        ),
    }
    return models


def evaluate_models(models, X_train, X_test, y_train, y_test, output_dir):
    """
    Trains each model, makes test predictions, and computes all classification metrics.
    """
    results_list = []
    confusion_matrices = {}

    print("=" * 75)
    print("MODEL TRAINING & EVALUATION RESULTS")
    print("=" * 75)

    for name, model in models.items():
        print(f"\nTraining: {name}...")
        model.fit(X_train, y_train)

        # Predict on unseen test set
        y_pred = model.predict(X_test)

        # Compute evaluation metrics
        acc = accuracy_score(y_test, y_pred)
        prec = precision_score(y_test, y_pred, zero_division=0)
        rec = recall_score(y_test, y_pred, zero_division=0)
        f1 = f1_score(y_test, y_pred, zero_division=0)
        cm = confusion_matrix(y_test, y_pred)
        tn, fp, fn, tp = cm.ravel()

        confusion_matrices[name] = cm

        results_list.append({
            "Model": name,
            "Accuracy": round(acc, 4),
            "Precision": round(prec, 4),
            "Recall": round(rec, 4),
            "F1_Score": round(f1, 4),
            "True_Negatives (TN)": int(tn),
            "False_Positives (FP)": int(fp),
            "False_Negatives (FN)": int(fn),
            "True_Positives (TP)": int(tp),
        })

        print(f"[{name}]")
        print(f"  Accuracy:  {acc * 100:.2f}%")
        print(f"  Precision: {prec * 100:.2f}%")
        print(f"  Recall:    {rec * 100:.2f}%")
        print(f"  F1-Score:  {f1 * 100:.2f}%")
        print(f"  Confusion Matrix: TN={tn}, FP={fp}, FN={fn}, TP={tp}")

    results_df = pd.DataFrame(results_list)
    results_csv = output_dir / "model_comparison_results.csv"
    results_df.to_csv(results_csv, index=False)
    print(f"\nSaved comparison results table to: {results_csv}")

    # Plot Confusion Matrices
    plot_confusion_matrices(confusion_matrices, output_dir)

    return results_df, models


def plot_confusion_matrices(cm_dict, output_dir):
    """Generates a visual comparison grid of confusion matrices."""
    fig, axes = plt.subplots(1, 3, figsize=(15, 4.5), dpi=300)
    labels = ["Safe (0)", "Victim (1)"]

    for ax, (name, cm) in zip(axes, cm_dict.items()):
        sns.heatmap(
            cm,
            annot=True,
            fmt="d",
            cmap="Blues",
            cbar=False,
            ax=ax,
            xticklabels=labels,
            yticklabels=labels,
            annot_kws={"size": 13, "weight": "bold"},
        )
        ax.set_title(f"{name}\nConfusion Matrix", fontsize=12, fontweight="bold", pad=10)
        ax.set_xlabel("Predicted Label", fontsize=10.5, fontweight="bold")
        ax.set_ylabel("True Ground Truth", fontsize=10.5, fontweight="bold")

    plt.tight_layout()
    cm_plot_path = output_dir / "07_model_confusion_matrices.png"
    plt.savefig(cm_plot_path, bbox_inches="tight")
    plt.close()
    print(f"Saved confusion matrix figure to: {cm_plot_path}")


def main():
    data_path, output_dir = get_paths()
    print("=" * 75)
    print("CYBER FRAUD RISK PREDICTION: MACHINE LEARNING PIPELINE")
    print("=" * 75)

    # 1. Load and Stratified Split
    X_train, X_test, y_train, y_test, feature_names = load_and_split_data(data_path)

    # 2. Build Models with Preprocessing
    models = build_models()

    # 3. Train & Evaluate Models
    results_df, trained_models = evaluate_models(
        models, X_train, X_test, y_train, y_test, output_dir
    )

    # 4. Feature Importance from Random Forest
    rf_model = trained_models["Random Forest"]
    importances = rf_model.feature_importances_
    feat_imp_df = pd.DataFrame({
        "Feature": feature_names,
        "Importance": importances,
    }).sort_values(by="Importance", ascending=False)

    feat_imp_path = output_dir / "random_forest_feature_importance.csv"
    feat_imp_df.to_csv(feat_imp_path, index=False)
    print(f"Saved Random Forest feature importances to: {feat_imp_path}")

    print("\n" + "=" * 75)
    print("FINAL MODEL PERFORMANCE COMPARISON TABLE")
    print("=" * 75)
    print(results_df.to_string(index=False))
    print("=" * 75)


if __name__ == "__main__":
    main()
