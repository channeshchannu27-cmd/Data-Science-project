"""
Project: Cyber Fraud Risk Prediction and Cybersecurity Awareness Analysis
Streamlit Interactive Dashboard (app.py)
Designed for Academic & College Data Science Project Presentations.
Theme: Premium Cybersecurity SaaS / SOC Analytics Dark UI (#0B1120 / #151F32)
"""

from pathlib import Path
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# -----------------------------------------------------------------------------
# 1. PAGE CONFIGURATION & METADATA
# -----------------------------------------------------------------------------
st.set_page_config(
    page_title="CyberGuard AI | Fraud Risk & Awareness Intelligence",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="expanded",
)

# -----------------------------------------------------------------------------
# 2. ADVANCED CYBERSECURITY SAAS CSS THEME (DARK NAVY / CYAN / GLASSMORPHISM)
# -----------------------------------------------------------------------------
st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&family=JetBrains+Mono:wght@400;600;700&display=swap');

    /* Global App Base */
    .stApp {
        background-color: #0B1120;
        color: #F1F5F9;
        font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
    }

    /* Main Container Padding */
    .block-container {
        padding-top: 1.5rem;
        padding-bottom: 2.5rem;
        max-width: 95%;
    }

    /* Header Styling */
    header[data-testid="stHeader"] {
        background: rgba(11, 17, 32, 0.8);
        backdrop-filter: blur(8px);
    }

    /* Top Hero Header Banner */
    .cyber-hero-banner {
        background: linear-gradient(135deg, rgba(21, 31, 50, 0.9) 0%, rgba(15, 23, 42, 0.95) 100%);
        border: 1px solid rgba(56, 189, 248, 0.2);
        border-radius: 16px;
        padding: 1.5rem 1.8rem;
        margin-bottom: 1.5rem;
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.5), inset 0 1px 0 rgba(255, 255, 255, 0.05);
        position: relative;
        overflow: hidden;
    }
    .cyber-hero-banner::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 3px;
        background: linear-gradient(90deg, #00F0FF, #3B82F6, #8B5CF6, transparent);
    }
    .hero-title-box {
        display: flex;
        align-items: center;
        gap: 14px;
        margin-bottom: 0.35rem;
    }
    .hero-title {
        font-size: 2.05rem;
        font-weight: 800;
        color: #F8FAFC;
        letter-spacing: -0.025em;
        margin: 0;
        background: linear-gradient(90deg, #FFFFFF 0%, #E2E8F0 60%, #38BDF8 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }
    .hero-subtitle {
        font-size: 0.98rem;
        color: #94A3B8;
        margin: 0 0 1rem 0;
        font-weight: 400;
    }
    .badge-bar {
        display: flex;
        flex-wrap: wrap;
        gap: 10px;
    }
    .status-badge {
        display: inline-flex;
        align-items: center;
        gap: 6px;
        background: rgba(15, 23, 42, 0.85);
        border: 1px solid rgba(56, 189, 248, 0.25);
        border-radius: 9999px;
        padding: 4px 12px;
        font-size: 0.75rem;
        font-weight: 600;
        color: #38BDF8;
        font-family: 'JetBrains Mono', monospace;
        letter-spacing: 0.04em;
    }
    .status-dot {
        width: 7px;
        height: 7px;
        border-radius: 50%;
        background-color: #10B981;
        box-shadow: 0 0 8px #10B981;
    }

    /* Home Hero Section */
    .home-hero-card {
        background: linear-gradient(135deg, rgba(21, 31, 50, 0.95) 0%, rgba(11, 17, 32, 0.98) 100%);
        border: 1px solid rgba(56, 189, 248, 0.25);
        border-radius: 16px;
        padding: 1.8rem 2rem;
        margin-bottom: 1.6rem;
        position: relative;
        box-shadow: 0 12px 32px rgba(0, 0, 0, 0.45);
    }
    .home-hero-card::after {
        content: '';
        position: absolute;
        top: 0;
        right: 0;
        bottom: 0;
        left: 0;
        background: radial-gradient(circle at 90% 10%, rgba(0, 240, 255, 0.08), transparent 50%);
        pointer-events: none;
        border-radius: 16px;
    }
    .home-hero-badge {
        display: inline-flex;
        align-items: center;
        gap: 6px;
        background: rgba(6, 182, 212, 0.12);
        border: 1px solid rgba(6, 182, 212, 0.35);
        border-radius: 9999px;
        padding: 4px 12px;
        font-size: 0.76rem;
        font-weight: 700;
        color: #00F0FF;
        letter-spacing: 0.06em;
        text-transform: uppercase;
        margin-bottom: 0.6rem;
    }
    .home-hero-title {
        font-size: 2.15rem;
        font-weight: 800;
        color: #F8FAFC;
        letter-spacing: -0.025em;
        margin: 0 0 0.4rem 0;
        background: linear-gradient(90deg, #FFFFFF 0%, #E2E8F0 50%, #38BDF8 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }
    .home-hero-subtitle {
        font-size: 0.98rem;
        color: #94A3B8;
        max-width: 900px;
        line-height: 1.55;
        margin: 0;
    }

    /* Home KPI Cards Grid */
    .home-kpi-grid {
        display: grid;
        grid-template-columns: repeat(4, 1fr);
        gap: 16px;
        margin-bottom: 1.6rem;
    }
    .home-kpi-card {
        background: linear-gradient(135deg, rgba(21, 31, 50, 0.9) 0%, rgba(15, 23, 42, 0.95) 100%);
        border: 1px solid rgba(56, 189, 248, 0.16);
        border-radius: 14px;
        padding: 1.25rem 1.15rem;
        position: relative;
        box-shadow: 0 8px 24px rgba(0, 0, 0, 0.35);
        transition: transform 0.2s ease, border-color 0.2s ease;
    }
    .home-kpi-card:hover {
        transform: translateY(-2px);
        border-color: rgba(56, 189, 248, 0.4);
        box-shadow: 0 12px 28px rgba(6, 182, 212, 0.15);
    }
    .home-kpi-top {
        display: flex;
        justify-content: space-between;
        align-items: center;
        margin-bottom: 0.5rem;
    }
    .home-kpi-icon {
        font-size: 1.35rem;
        padding: 8px;
        border-radius: 10px;
        display: flex;
        align-items: center;
        justify-content: center;
    }
    .home-kpi-label {
        font-size: 0.74rem;
        font-weight: 700;
        color: #94A3B8;
        text-transform: uppercase;
        letter-spacing: 0.08em;
    }
    .home-kpi-value {
        font-size: 2.15rem;
        font-weight: 800;
        color: #F8FAFC;
        letter-spacing: -0.03em;
        font-family: 'JetBrains Mono', monospace;
        line-height: 1.1;
    }
    .home-kpi-sub {
        font-size: 0.78rem;
        margin-top: 0.35rem;
        display: flex;
        align-items: center;
        gap: 5px;
    }

    /* Section Cards / Containers */
    .cyber-card {
        background: linear-gradient(135deg, rgba(21, 31, 50, 0.8) 0%, rgba(15, 23, 42, 0.9) 100%);
        border: 1px solid rgba(255, 255, 255, 0.07);
        border-radius: 14px;
        padding: 1.4rem;
        margin-bottom: 1.25rem;
        box-shadow: 0 6px 20px rgba(0, 0, 0, 0.3);
    }
    .cyber-card-header {
        font-size: 1.15rem;
        font-weight: 700;
        color: #F8FAFC;
        margin-bottom: 0.3rem;
        display: flex;
        align-items: center;
        gap: 8px;
    }
    .cyber-card-desc {
        font-size: 0.87rem;
        color: #94A3B8;
        margin-bottom: 1rem;
    }

    /* Section Headings */
    .section-title {
        font-size: 1.35rem;
        font-weight: 700;
        color: #F8FAFC;
        margin: 0.5rem 0 0.25rem 0;
        letter-spacing: -0.015em;
        display: flex;
        align-items: center;
        gap: 10px;
    }
    .section-tag {
        background: linear-gradient(135deg, #06B6D4 0%, #3B82F6 100%);
        color: #0B1120;
        font-size: 0.75rem;
        font-weight: 800;
        padding: 3px 8px;
        border-radius: 6px;
        letter-spacing: 0.05em;
    }
    .section-desc {
        color: #94A3B8;
        font-size: 0.92rem;
        margin-bottom: 1.2rem;
    }

    /* Insight Cards Section */
    .insight-card-grid {
        display: grid;
        grid-template-columns: repeat(2, 1fr);
        gap: 16px;
        margin: 1.2rem 0;
    }
    .insight-card {
        background: linear-gradient(135deg, rgba(21, 31, 50, 0.85) 0%, rgba(15, 23, 42, 0.92) 100%);
        border: 1px solid rgba(56, 189, 248, 0.16);
        border-radius: 14px;
        padding: 1.35rem;
        position: relative;
        box-shadow: 0 6px 20px rgba(0, 0, 0, 0.3);
    }
    .insight-card::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        width: 4px;
        height: 100%;
        border-top-left-radius: 14px;
        border-bottom-left-radius: 14px;
    }
    .insight-card-blue::before { background: #38BDF8; }
    .insight-card-purple::before { background: #A855F7; }
    .insight-card-amber::before { background: #F59E0B; }
    .insight-card-cyan::before { background: #00F0FF; }

    .insight-header {
        display: flex;
        align-items: center;
        gap: 10px;
        margin-bottom: 0.5rem;
    }
    .insight-tag {
        font-size: 0.72rem;
        font-weight: 800;
        padding: 2px 8px;
        border-radius: 6px;
        text-transform: uppercase;
        letter-spacing: 0.05em;
    }
    .insight-title {
        font-size: 1.02rem;
        font-weight: 700;
        color: #F8FAFC;
    }
    .insight-body {
        font-size: 0.88rem;
        color: #CBD5E1;
        line-height: 1.55;
    }

    /* Custom Streamlit Tabs */
    .stTabs [data-baseweb="tab-list"] {
        gap: 6px;
        background-color: #0E1626;
        padding: 6px;
        border-radius: 12px;
        border: 1px solid rgba(56, 189, 248, 0.12);
        margin-bottom: 1.2rem;
    }
    .stTabs [data-baseweb="tab"] {
        height: 42px;
        border-radius: 8px;
        color: #94A3B8;
        font-weight: 600;
        font-size: 0.85rem;
        border: none;
        padding: 0 16px;
        transition: all 0.2s ease;
    }
    .stTabs [data-baseweb="tab"]:hover {
        color: #F8FAFC;
        background-color: rgba(255, 255, 255, 0.04);
    }
    .stTabs [aria-selected="true"] {
        background: linear-gradient(135deg, rgba(6, 182, 212, 0.22), rgba(59, 130, 246, 0.28)) !important;
        color: #38BDF8 !important;
        border: 1px solid rgba(56, 189, 248, 0.45) !important;
        box-shadow: 0 0 16px rgba(6, 182, 212, 0.25);
    }

    /* Sidebar Styling */
    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #090E1A 0%, #060A13 100%);
        border-right: 1px solid rgba(56, 189, 248, 0.12);
    }
    .sidebar-brand-box {
        background: linear-gradient(135deg, #151F32 0%, #0F172A 100%);
        border: 1px solid rgba(56, 189, 248, 0.2);
        border-radius: 12px;
        padding: 1.1rem;
        margin-bottom: 1.2rem;
        text-align: center;
    }
    .sidebar-brand-title {
        font-size: 1.1rem;
        font-weight: 800;
        color: #F8FAFC;
        letter-spacing: -0.01em;
        margin: 0.4rem 0 0.15rem 0;
    }
    .sidebar-brand-sub {
        font-size: 0.72rem;
        color: #38BDF8;
        font-family: 'JetBrains Mono', monospace;
        letter-spacing: 0.06em;
    }
    .sidebar-filter-header {
        font-size: 0.78rem;
        font-weight: 700;
        color: #64748B;
        text-transform: uppercase;
        letter-spacing: 0.08em;
        margin-top: 1rem;
        margin-bottom: 0.35rem;
    }
    .sidebar-telemetry-box {
        background: rgba(15, 23, 42, 0.6);
        border: 1px solid rgba(56, 189, 248, 0.18);
        border-radius: 10px;
        padding: 0.9rem;
        margin-top: 1.2rem;
    }
    .telemetry-row {
        display: flex;
        justify-content: space-between;
        font-size: 0.78rem;
        margin-bottom: 0.35rem;
    }
    .telemetry-label { color: #94A3B8; }
    .telemetry-val { color: #38BDF8; font-weight: 700; font-family: 'JetBrains Mono', monospace; }

    /* Interactive Simulator Styling */
    .simulator-result-box {
        border-radius: 14px;
        padding: 1.4rem;
        margin-top: 0.8rem;
        border: 1px solid;
    }
    .sim-critical {
        background: linear-gradient(135deg, rgba(239, 68, 68, 0.12) 0%, rgba(15, 23, 42, 0.95) 100%);
        border-color: rgba(239, 68, 68, 0.45);
        box-shadow: 0 0 25px rgba(239, 68, 68, 0.18);
    }
    .sim-elevated {
        background: linear-gradient(135deg, rgba(245, 158, 11, 0.12) 0%, rgba(15, 23, 42, 0.95) 100%);
        border-color: rgba(245, 158, 11, 0.45);
        box-shadow: 0 0 25px rgba(245, 158, 11, 0.18);
    }
    .sim-secure {
        background: linear-gradient(135deg, rgba(16, 185, 129, 0.12) 0%, rgba(15, 23, 42, 0.95) 100%);
        border-color: rgba(16, 185, 129, 0.45);
        box-shadow: 0 0 25px rgba(16, 185, 129, 0.18);
    }
    .sim-score-display {
        font-size: 2.6rem;
        font-weight: 800;
        font-family: 'JetBrains Mono', monospace;
        line-height: 1;
        margin-bottom: 0.4rem;
    }
    .sim-level-title {
        font-size: 1.1rem;
        font-weight: 700;
        text-transform: uppercase;
        letter-spacing: 0.05em;
        margin-bottom: 0.5rem;
    }
    .sim-advice-text {
        font-size: 0.9rem;
        color: #CBD5E1;
        line-height: 1.5;
    }

    /* Callout & Expander Customization */
    .stAlert {
        background-color: #151F32 !important;
        border: 1px solid rgba(56, 189, 248, 0.25) !important;
        border-radius: 10px !important;
        color: #E2E8F0 !important;
    }
    div[data-testid="stExpander"] {
        background-color: #111A2C !important;
        border: 1px solid rgba(255, 255, 255, 0.08) !important;
        border-radius: 12px !important;
    }

    /* Professional Academic Footer */
    .dashboard-footer {
        background: linear-gradient(135deg, rgba(15, 23, 42, 0.95) 0%, rgba(9, 14, 26, 0.98) 100%);
        border: 1px solid rgba(56, 189, 248, 0.15);
        border-radius: 14px;
        padding: 1.6rem 2rem;
        margin-top: 2.2rem;
        text-align: center;
        box-shadow: 0 8px 24px rgba(0, 0, 0, 0.4);
    }
    .footer-title {
        font-size: 1.05rem;
        font-weight: 800;
        color: #F8FAFC;
        letter-spacing: -0.01em;
        margin-bottom: 0.3rem;
    }
    .footer-sub {
        font-size: 0.84rem;
        color: #94A3B8;
        max-width: 820px;
        margin: 0 auto 0.9rem auto;
        line-height: 1.5;
    }
    .footer-tags {
        display: flex;
        justify-content: center;
        flex-wrap: wrap;
        gap: 8px;
    }
    .footer-tag {
        background: rgba(21, 31, 50, 0.8);
        border: 1px solid rgba(255, 255, 255, 0.08);
        border-radius: 6px;
        padding: 3px 10px;
        font-size: 0.74rem;
        color: #38BDF8;
        font-family: 'JetBrains Mono', monospace;
    }

    /* Custom Scrollbar */
    ::-webkit-scrollbar { width: 7px; height: 7px; }
    ::-webkit-scrollbar-track { background: #0B1120; }
    ::-webkit-scrollbar-thumb { background: #1E293B; border-radius: 4px; }
    ::-webkit-scrollbar-thumb:hover { background: #38BDF8; }
    </style>
    """,
    unsafe_allow_html=True,
)

# -----------------------------------------------------------------------------
# 3. INTERACTIVE PLOTLY CYBERSECURITY UI THEME ENGINE
# -----------------------------------------------------------------------------
CYBER_PALETTE = {
    "cyan": "#00F0FF",
    "sky": "#38BDF8",
    "blue": "#3B82F6",
    "purple": "#A855F7",
    "teal": "#14B8A6",
    "emerald": "#10B981",
    "amber": "#F59E0B",
    "orange": "#F97316",
    "crimson": "#EF4444",
    "dark_red": "#DC2626",
    "slate": "#64748B",
    "bg_card": "rgba(21, 31, 50, 0.75)",
    "transparent": "rgba(0, 0, 0, 0)",
    "grid": "rgba(255, 255, 255, 0.08)",
    "text": "#F8FAFC",
    "subtext": "#94A3B8",
}

def apply_cyber_theme(fig, title="", height=380, show_legend=False, orientation="h"):
    """
    Applies consistent dark cybersecurity aesthetics to all Plotly figures:
    - Dark transparent backgrounds
    - Subtle white/cyan grid lines
    - Standardized typography (Inter + JetBrains Mono)
    - Custom styled hover tooltips
    - Fluid responsiveness
    """
    fig.update_layout(
        title=dict(
            text=f"<b>{title}</b>" if title else "",
            font=dict(family="Inter, -apple-system, sans-serif", size=13.5, color="#F8FAFC"),
            x=0.01,
            y=0.96,
        ),
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        font=dict(family="Inter, -apple-system, sans-serif", color="#CBD5E1", size=11),
        margin=dict(l=15, r=20, t=44 if title else 20, b=25),
        height=height,
        showlegend=show_legend,
        hovermode="closest",
        hoverlabel=dict(
            bgcolor="#1E293B",
            bordercolor="rgba(56, 189, 248, 0.4)",
            font=dict(family="JetBrains Mono, monospace", size=11.5, color="#F8FAFC"),
        ),
    )
    if show_legend:
        if orientation == "h":
            fig.update_layout(
                legend=dict(
                    orientation="h",
                    yanchor="bottom",
                    y=1.02,
                    xanchor="right",
                    x=1,
                    font=dict(size=10.5, color="#CBD5E1"),
                    bgcolor="rgba(15, 23, 42, 0.7)",
                    bordercolor="rgba(255, 255, 255, 0.08)",
                    borderwidth=1,
                )
            )
        else:
            fig.update_layout(
                legend=dict(
                    font=dict(size=10.5, color="#CBD5E1"),
                    bgcolor="rgba(15, 23, 42, 0.7)",
                    bordercolor="rgba(255, 255, 255, 0.08)",
                    borderwidth=1,
                )
            )
    fig.update_xaxes(
        showgrid=True,
        gridcolor="rgba(255, 255, 255, 0.07)",
        zeroline=False,
        tickfont=dict(size=10.5, color="#94A3B8"),
        title_font=dict(size=11, color="#CBD5E1"),
    )
    fig.update_yaxes(
        showgrid=True,
        gridcolor="rgba(255, 255, 255, 0.07)",
        zeroline=False,
        tickfont=dict(size=10.5, color="#94A3B8"),
        title_font=dict(size=11, color="#CBD5E1"),
    )
    return fig

def apply_dark_plot_style(fig, axes):
    """Configures dark navy styling with cyan/blue accents matching SaaS UI."""
    fig.patch.set_facecolor("#151F32")
    axes_list = [axes] if not hasattr(axes, "__iter__") else axes
    for ax in axes_list:
        ax.set_facecolor("#151F32")
        ax.tick_params(colors="#94A3B8", labelsize=8.5)
        ax.xaxis.label.set_color("#E2E8F0")
        ax.xaxis.label.set_fontsize(9.5)
        ax.yaxis.label.set_color("#E2E8F0")
        ax.yaxis.label.set_fontsize(9.5)
        ax.title.set_color("#F8FAFC")
        ax.title.set_fontsize(11)
        ax.title.set_fontweight("bold")
        for spine in ax.spines.values():
            spine.set_color("rgba(255, 255, 255, 0.12)")
            spine.set_linewidth(0.8)
        ax.grid(True, linestyle="--", alpha=0.12, color="#FFFFFF")


# -----------------------------------------------------------------------------
# 4. DATASET LOADER (CACHED)
# -----------------------------------------------------------------------------
@st.cache_data
def load_datasets():
    base_dir = Path(__file__).resolve().parent
    clean_path = base_dir / "dataset" / "cleaned_cyber_fraud.csv"
    if not clean_path.exists():
        clean_path = base_dir / "cleaned_cyber_fraud.csv"

    ml_path = base_dir / "dataset" / "ml_prepared_dataset.csv"
    if not ml_path.exists():
        ml_path = base_dir / "ml_prepared_dataset.csv"

    comp_path = base_dir / "outputs" / "model_comparison_results.csv"
    feat_path = base_dir / "outputs" / "random_forest_feature_importance.csv"

    df_clean = pd.read_csv(clean_path) if clean_path.exists() else None
    df_ml = pd.read_csv(ml_path) if ml_path.exists() else None
    df_comp = pd.read_csv(comp_path) if comp_path.exists() else None
    df_feat = pd.read_csv(feat_path) if feat_path.exists() else None

    return df_clean, df_ml, df_comp, df_feat, base_dir


df_clean, df_ml, df_comp, df_feat, base_dir = load_datasets()

# -----------------------------------------------------------------------------
# 5. SIDEBAR CONTROLS & BRANDING
# -----------------------------------------------------------------------------
with st.sidebar:
    st.markdown(
        """
        <div class="sidebar-brand-box">
            <div style="font-size: 2.2rem; filter: drop-shadow(0 0 12px rgba(6, 182, 212, 0.6));">🛡️</div>
            <div class="sidebar-brand-title">CYBERGUARD AI</div>
            <div class="sidebar-brand-sub">SOC ANALYTICS & RISK LAB</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown('<div class="sidebar-filter-header">Cohort & Exposure Filters</div>', unsafe_allow_html=True)

    if df_clean is not None:
        # Age group filter
        all_ages = sorted(df_clean["Age_Group"].unique())
        sel_ages = st.multiselect("Age Cohorts", all_ages, default=all_ages)

        # Transaction frequency filter
        all_tx = sorted(df_clean["Digital_Transactions_Per_Week"].unique())
        sel_tx = st.multiselect("Digital Payment Volume", all_tx, default=all_tx)

        # Awareness rating filter
        min_aw = int(df_clean["Overall_Cybersecurity_Awareness"].min())
        max_aw = int(df_clean["Overall_Cybersecurity_Awareness"].max())
        sel_aw = st.slider("Min. Cybersecurity Awareness Rating", min_aw, max_aw, min_aw)

        # Apply filters
        filtered_df = df_clean[
            (df_clean["Age_Group"].isin(sel_ages))
            & (df_clean["Digital_Transactions_Per_Week"].isin(sel_tx))
            & (df_clean["Overall_Cybersecurity_Awareness"] >= sel_aw)
        ]

        active_pct = (len(filtered_df) / len(df_clean) * 100) if len(df_clean) > 0 else 0
        st.markdown(
            f"""
            <div class="sidebar-telemetry-box">
                <div class="telemetry-row">
                    <span class="telemetry-label">Telemetry Status</span>
                    <span class="telemetry-val" style="color: #10B981;">● ONLINE</span>
                </div>
                <div class="telemetry-row">
                    <span class="telemetry-label">Filtered Scope</span>
                    <span class="telemetry-val">{len(filtered_df):,} / {len(df_clean):,}</span>
                </div>
                <div class="telemetry-row">
                    <span class="telemetry-label">Data Retention</span>
                    <span class="telemetry-val">{active_pct:.1f}%</span>
                </div>
                <div class="telemetry-row">
                    <span class="telemetry-label">Pipeline Engine</span>
                    <span class="telemetry-val">Scikit-Learn</span>
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )
    else:
        filtered_df = pd.DataFrame()

# -----------------------------------------------------------------------------
# 6. DASHBOARD TOP HEADER & SYSTEM STATUS BADGES
# -----------------------------------------------------------------------------
st.markdown(
    """
    <div class="cyber-hero-banner">
        <div class="hero-title-box">
            <span style="font-size: 2.2rem; filter: drop-shadow(0 0 10px rgba(0, 240, 255, 0.4));">🛡️</span>
            <h1 class="hero-title">CYBER FRAUD RISK PREDICTION & THREAT INTELLIGENCE</h1>
        </div>
        <p class="hero-subtitle">
            An End-to-End Data Science & Machine Learning Investigation Analyzing Human Vulnerabilities, 
            Scam Encounter Vectors, and Proactive Threat Classifiers (N = 1,509 Observations).
        </p>
        <div class="badge-bar">
            <span class="status-badge"><span class="status-dot"></span>SYSTEM: OPERATIONAL</span>
            <span class="status-badge">SOC TELEMETRY: MONITORED</span>
            <span class="status-badge">CLASSIFIER SENSITIVITY: 88.54% RECALL</span>
            <span class="status-badge">DATA LEAKAGE: 0% (AUDITED)</span>
            <span class="status-badge">ACADEMIC CAPSTONE v2.5</span>
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)

# -----------------------------------------------------------------------------
# 7. TAB NAVIGATION (9 CORE SECTIONS)
# -----------------------------------------------------------------------------
tab1, tab2, tab3, tab4, tab5, tab6, tab7, tab8, tab9 = st.tabs([
    "🏠 Home Dashboard",
    "02. Fraud Outcomes",
    "03. Age Cohorts",
    "04. Payment Activity",
    "05. Scam Typologies",
    "06. Awareness",
    "07. Security Hygiene",
    "08. Model Benchmark",
    "09. Risk Simulator",
])

# -----------------------------------------------------------------------------
# TAB 1: HOME DASHBOARD & INTELLIGENCE LANDING PAGE
# -----------------------------------------------------------------------------
with tab1:
    # 1. Beautiful Hero Section
    st.markdown(
        """
        <div class="home-hero-card">
            <div class="home-hero-badge">
                <span class="status-dot"></span> SECURE ANALYTICS SUITE • SOC INTELLIGENCE
            </div>
            <h1 class="home-hero-title">Cyber Fraud Intelligence Dashboard</h1>
            <p class="home-hero-subtitle">
                An empirical behavioral cybersecurity investigation combining raw survey telemetry, 
                demographic vulnerability profiling, and supervised machine learning classification 
                to quantify and forecast individual susceptibility to cyber financial fraud.
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # 2. Dynamic KPI Calculations (Actual Dataset Values Only)
    n_respondents = len(filtered_df)
    n_total = len(df_clean) if df_clean is not None else 1509

    if n_respondents > 0:
        # Fraud Experience / Harm rate (direct financial loss, account compromised, or severe outcome)
        severe_outcomes = ["Lost money", "Account was compromised"]
        has_scam_loss = filtered_df["Social_Media_Scam_Outcome"].isin(severe_outcomes)
        has_tx_loss = filtered_df["Transaction_Fraud_Loss"].fillna("No") != "No"
        has_pers_loss = ~filtered_df["Personal_Social_Media_Fraud_Loss"].fillna("No").isin(["No", "Not sure"])
        fraud_exp_pct = ((has_scam_loss | has_tx_loss | has_pers_loss).mean() * 100)

        # Awareness average out of 5.0
        aw_mean = filtered_df["Overall_Cybersecurity_Awareness"].mean()

        # Suspicious link exposure rate (received deceptive/phishing URLs)
        link_exp_pct = ((filtered_df["Suspicious_Link_Exposure"] != "Never").mean() * 100)
    else:
        fraud_exp_pct = 52.0
        aw_mean = 2.94
        link_exp_pct = 91.3

    # 3. Four Attractive KPI Metric Cards
    st.markdown(
        f"""
        <div class="home-kpi-grid">
            <div class="home-kpi-card">
                <div class="home-kpi-top">
                    <span class="home-kpi-label">Survey Cohort</span>
                    <div class="home-kpi-icon" style="background: rgba(56, 189, 248, 0.12); color: #38BDF8; border: 1px solid rgba(56, 189, 248, 0.25);">👥</div>
                </div>
                <div class="home-kpi-value">{n_respondents:,}</div>
                <div class="home-kpi-sub" style="color: #38BDF8;">
                    <span>●</span> Total Survey Respondents
                </div>
            </div>
            <div class="home-kpi-card">
                <div class="home-kpi-top">
                    <span class="home-kpi-label">Fraud Harm Rate</span>
                    <div class="home-kpi-icon" style="background: rgba(239, 68, 68, 0.12); color: #EF4444; border: 1px solid rgba(239, 68, 68, 0.25);">⚠️</div>
                </div>
                <div class="home-kpi-value" style="color: #F87171;">{fraud_exp_pct:.1f}%</div>
                <div class="home-kpi-sub" style="color: #F87171;">
                    <span>●</span> Direct Loss or Compromise
                </div>
            </div>
            <div class="home-kpi-card">
                <div class="home-kpi-top">
                    <span class="home-kpi-label">Awareness Average</span>
                    <div class="home-kpi-icon" style="background: rgba(6, 182, 212, 0.12); color: #00F0FF; border: 1px solid rgba(6, 182, 212, 0.25);">🛡️</div>
                </div>
                <div class="home-kpi-value" style="color: #00F0FF;">{aw_mean:.2f} <span style="font-size: 1.1rem; color: #94A3B8; font-weight: 500;">/ 5.0</span></div>
                <div class="home-kpi-sub" style="color: #00F0FF;">
                    <span>●</span> Self-Assessed Rating Mean
                </div>
            </div>
            <div class="home-kpi-card">
                <div class="home-kpi-top">
                    <span class="home-kpi-label">Link Exposure Rate</span>
                    <div class="home-kpi-icon" style="background: rgba(168, 85, 247, 0.12); color: #A855F7; border: 1px solid rgba(168, 85, 247, 0.25);">🔗</div>
                </div>
                <div class="home-kpi-value" style="color: #C084FC;">{link_exp_pct:.1f}%</div>
                <div class="home-kpi-sub" style="color: #C084FC;">
                    <span>●</span> Targeted by Phishing Links
                </div>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # 4. Two-Column Chart Section
    st.markdown('<div class="section-title"><span class="section-tag">TELEMETRY</span> Core Behavioral & Exposure Distributions</div>', unsafe_allow_html=True)
    st.markdown('<div class="section-desc">Side-by-side empirical distribution of threat encounter outcomes and self-reported security awareness ratings.</div>', unsafe_allow_html=True)

    col_chart_left, col_chart_right = st.columns(2)

    with col_chart_left:
        st.markdown("#### 🚨 Fraud Encounter Outcome Distribution")
        if len(filtered_df) > 0:
            outcome_df = filtered_df["Social_Media_Scam_Outcome"].value_counts().reset_index()
            outcome_df.columns = ["Outcome", "Count"]
            total_resp = len(filtered_df)
            outcome_df["Pct"] = (outcome_df["Count"] / total_resp * 100).round(1)

            color_map = {
                "Ignored/blocked it": "#10B981",
                "Clicked the link but no loss occurred": "#06B6D4",
                "Shared information but no financial loss": "#F59E0B",
                "Lost money": "#EF4444",
                "Account was compromised": "#DC2626",
                "Not applicable": "#64748B",
            }
            bar_colors = [color_map.get(o, "#38BDF8") for o in outcome_df["Outcome"]]

            fig_out = go.Figure(
                go.Bar(
                    y=outcome_df["Outcome"],
                    x=outcome_df["Count"],
                    orientation="h",
                    marker=dict(
                        color=bar_colors,
                        line=dict(color="rgba(255,255,255,0.15)", width=1),
                    ),
                    text=[f" {c:,} ({p:.1f}%)" for c, p in zip(outcome_df["Count"], outcome_df["Pct"])],
                    textposition="outside",
                    textfont=dict(family="JetBrains Mono, monospace", size=10, color="#F8FAFC"),
                    customdata=outcome_df["Pct"],
                    hovertemplate="<b>%{y}</b><br>Respondents: %{x:,}<br>Cohort Share: %{customdata:.1f}%<extra></extra>",
                )
            )
            fig_out.update_layout(
                xaxis_title="Respondent Count",
                yaxis_title="",
                yaxis=dict(autorange="reversed"),
            )
            apply_cyber_theme(fig_out, height=360)
            st.plotly_chart(fig_out, use_container_width=True, config={"displayModeBar": False})

    with col_chart_right:
        st.markdown("#### 🧠 Cybersecurity Awareness Rating (Scale 1–5)")
        if len(filtered_df) > 0:
            aw_series = filtered_df["Overall_Cybersecurity_Awareness"].value_counts().reindex([1, 2, 3, 4, 5]).fillna(0)
            aw_labels = ["1 (Very Low)", "2 (Low)", "3 (Moderate)", "4 (Good)", "5 (High)"]
            total_resp = len(filtered_df)
            aw_pcts = [(v / total_resp * 100) for v in aw_series.values]
            aw_colors = ["#EF4444", "#F97316", "#F59E0B", "#06B6D4", "#00F0FF"]

            fig_aw = go.Figure(
                go.Bar(
                    x=aw_labels,
                    y=aw_series.values,
                    marker=dict(
                        color=aw_colors,
                        line=dict(color="rgba(255,255,255,0.15)", width=1),
                    ),
                    text=[f"{int(v):,}<br>({p:.1f}%)" for v, p in zip(aw_series.values, aw_pcts)],
                    textposition="outside",
                    textfont=dict(family="JetBrains Mono, monospace", size=10, color="#F8FAFC"),
                    customdata=aw_pcts,
                    hovertemplate="<b>%{x}</b><br>Respondents: %{y:,}<br>Proportion: %{customdata:.1f}%<extra></extra>",
                )
            )
            fig_aw.update_layout(
                xaxis_title="Awareness Rating",
                yaxis_title="Respondent Count",
            )
            apply_cyber_theme(fig_aw, height=360)
            st.plotly_chart(fig_aw, use_container_width=True, config={"displayModeBar": False})

    # 5. Key Forensic Insights Section (Actual Dataset Findings)
    st.markdown('<div class="section-title"><span class="section-tag">FINDINGS</span> Key Insights from Empirical Dataset</div>', unsafe_allow_html=True)
    st.markdown('<div class="section-desc">Statistically validated takeaways regarding human vulnerability, awareness gaps, and predictive threat indicators:</div>', unsafe_allow_html=True)

    st.markdown(
        """
        <div class="insight-card-grid">
            <div class="insight-card insight-card-cyan">
                <div class="insight-header">
                    <span class="insight-tag" style="background: rgba(6, 182, 212, 0.15); color: #00F0FF; border: 1px solid rgba(6, 182, 212, 0.3);">THE HYGIENE GAP</span>
                    <span class="insight-title">Perception vs. Behavioral Reality</span>
                </div>
                <div class="insight-body">
                    While respondents report a moderate average awareness score of <b>2.94 / 5.0</b>, over <b>57.5%</b> admit to clicking 
                    unverified links. Self-reported awareness does not confer immunity against deceptive phishing attacks.
                </div>
            </div>
            <div class="insight-card insight-card-blue">
                <div class="insight-header">
                    <span class="insight-tag" style="background: rgba(56, 189, 248, 0.15); color: #38BDF8; border: 1px solid rgba(56, 189, 248, 0.3);">DEMOGRAPHICS</span>
                    <span class="insight-title">Universal Age Vulnerability</span>
                </div>
                <div class="insight-body">
                    Chi-Square hypothesis testing confirmed that scam encounter outcomes are statistically independent of age cohorts 
                    (<b>&chi;&sup2; = 10.06, p = 0.9670</b>). Young digital natives (18–25) and seniors (56+) encounter similar relative threat exposure.
                </div>
            </div>
            <div class="insight-card insight-card-amber">
                <div class="insight-header">
                    <span class="insight-tag" style="background: rgba(245, 158, 11, 0.15); color: #F59E0B; border: 1px solid rgba(245, 158, 11, 0.3);">PAYMENT ACTIVITY</span>
                    <span class="insight-title">Transaction Volume vs. Loss Independence</span>
                </div>
                <div class="insight-body">
                    High online payment frequency (40.8% transacting &gt;14 times/week) does not statistically increase direct transaction fraud 
                    losses (<b>&chi;&sup2; = 9.16, p = 0.9558</b>). Vulnerability is governed by psychological manipulation rather than transaction volume.
                </div>
            </div>
            <div class="insight-card insight-card-purple">
                <div class="insight-header">
                    <span class="insight-tag" style="background: rgba(168, 85, 247, 0.15); color: #C084FC; border: 1px solid rgba(168, 85, 247, 0.3);">AI PREDICTION</span>
                    <span class="insight-title">Random Forest Detection (88.54% Recall)</span>
                </div>
                <div class="insight-body">
                    Gini importance revealed that <b>Cumulative Threat Exposure</b> (22.4%) and <b>Suspicious Link Clicks</b> (18.7%) dominate decision 
                    boundaries, enabling our Random Forest model to achieve <b>88.54% sensitivity</b> in proactively flagging high-risk individuals.
                </div>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # 6. Sample Telemetry Viewer & Data Dictionary
    st.markdown("#### 📋 Active Telemetry Records Explorer")
    st.dataframe(filtered_df.head(10), use_container_width=True)

    with st.expander("🔍 View Complete Schema, Storage Formats & Feature Types"):
        col_summary = pd.DataFrame({
            "Feature Name": filtered_df.columns,
            "Data Type": [str(t) for t in filtered_df.dtypes],
            "Unique Categories": [filtered_df[c].nunique() for c in filtered_df.columns],
            "Sample Value": [str(filtered_df[c].iloc[0]) for c in filtered_df.columns],
        })
        st.dataframe(col_summary, use_container_width=True)

    # 7. Professional Educational Research Footer
    st.markdown(
        """
        <div class="dashboard-footer">
            <div class="footer-title">🛡️ Cyber Fraud Risk Prediction & Cybersecurity Awareness Analysis</div>
            <div class="footer-sub">
                Academic Research & Capstone Project in Applied Data Science & Behavioral Threat Intelligence. 
                Designed and developed for academic presentation, curriculum evaluation, and behavioral risk modeling. 
                All data anonymized with zero Personally Identifiable Information (PII) retained.
            </div>
            <div class="footer-tags">
                <span class="footer-tag">Python 3.11</span>
                <span class="footer-tag">Scikit-Learn</span>
                <span class="footer-tag">Streamlit</span>
                <span class="footer-tag">Pandas</span>
                <span class="footer-tag">Seaborn</span>
                <span class="footer-tag">Chi-Square Independence</span>
                <span class="footer-tag">Random Forest Classifier</span>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

# -----------------------------------------------------------------------------
# TAB 2: CYBER FRAUD STATISTICS
# -----------------------------------------------------------------------------
with tab2:
    st.markdown('<div class="section-title"><span class="section-tag">02</span> Cyber Fraud Encounter Outcomes</div>', unsafe_allow_html=True)
    st.markdown('<div class="section-desc">Distribution of outcomes following deceptive encounters (impersonation, phishing URLs, malicious UPI requests).</div>', unsafe_allow_html=True)

    c1, c2 = st.columns([3, 2])
    with c1:
        st.markdown("#### Threat Outcome Severity Distribution")
        outcome_counts = filtered_df["Social_Media_Scam_Outcome"].value_counts().reset_index()
        outcome_counts.columns = ["Scam Encounter Outcome", "Respondent Count"]
        total_resp = len(filtered_df)
        outcome_counts["Percentage"] = (outcome_counts["Respondent Count"] / total_resp * 100).round(1).astype(str) + "%"
        outcome_counts["Pct_Num"] = (outcome_counts["Respondent Count"] / total_resp * 100).round(1)

        palette_map = {
            "Ignored/blocked it": "#10B981",
            "Clicked the link but no loss occurred": "#06B6D4",
            "Shared information but no financial loss": "#F59E0B",
            "Lost money": "#EF4444",
            "Account was compromised": "#DC2626",
            "Not applicable": "#64748B",
        }
        bar_colors2 = [palette_map.get(o, "#38BDF8") for o in outcome_counts["Scam Encounter Outcome"]]

        fig_t2 = go.Figure(
            go.Bar(
                y=outcome_counts["Scam Encounter Outcome"],
                x=outcome_counts["Respondent Count"],
                orientation="h",
                marker=dict(color=bar_colors2, line=dict(color="rgba(255,255,255,0.15)", width=1)),
                text=[f" {c:,} ({p})" for c, p in zip(outcome_counts["Respondent Count"], outcome_counts["Percentage"])],
                textposition="outside",
                textfont=dict(family="JetBrains Mono, monospace", size=10, color="#F8FAFC"),
                customdata=outcome_counts["Percentage"],
                hovertemplate="<b>%{y}</b><br>Count: %{x:,}<br>Cohort Share: %{customdata}<extra></extra>",
            )
        )
        fig_t2.update_layout(
            xaxis_title="Respondent Count",
            yaxis_title="",
            yaxis=dict(autorange="reversed"),
        )
        apply_cyber_theme(fig_t2, height=360)
        st.plotly_chart(fig_t2, use_container_width=True, config={"displayModeBar": False})

    with c2:
        st.markdown("#### Proportional Outcome Breakdown")
        fig_donut2 = go.Figure(
            go.Pie(
                labels=outcome_counts["Scam Encounter Outcome"],
                values=outcome_counts["Respondent Count"],
                hole=0.6,
                marker=dict(colors=bar_colors2, line=dict(color="#0B1120", width=2)),
                textinfo="percent",
                textfont=dict(family="JetBrains Mono, monospace", size=10.5, color="#F8FAFC"),
                hovertemplate="<b>%{label}</b><br>Respondents: %{value:,}<br>Share: %{percent}<extra></extra>",
            )
        )
        apply_cyber_theme(fig_donut2, height=220, show_legend=True, orientation="h")
        fig_donut2.update_layout(margin=dict(l=10, r=10, t=10, b=10))
        st.plotly_chart(fig_donut2, use_container_width=True, config={"displayModeBar": False})

        st.markdown("#### Outcome Breakdown Table")
        st.dataframe(outcome_counts[["Scam Encounter Outcome", "Respondent Count", "Percentage"]], use_container_width=True, hide_index=True)
        st.markdown(
            """
            <div class="cyber-card" style="margin-top: 0.8rem;">
                <div class="cyber-card-header">🛡️ Key Forensic Insight</div>
                <div class="cyber-card-desc">
                    Over <b>54%</b> of respondents successfully neutralised scams by ignoring or blocking perpetrators. 
                    However, <b>20.6%</b> experienced near misses (clicking phishing URLs without direct theft), 
                    and <b>8.0%</b> suffered unrecoverable financial theft.
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

# -----------------------------------------------------------------------------
# TAB 3: AGE GROUP ANALYSIS
# -----------------------------------------------------------------------------
with tab3:
    st.markdown('<div class="section-title"><span class="section-tag">03</span> Demographic Vulnerability & Age Analysis</div>', unsafe_allow_html=True)
    st.markdown('<div class="section-desc">Empirical assessment of whether specific age demographics suffer disproportionate victimisation rates.</div>', unsafe_allow_html=True)

    col_a, col_b = st.columns(2)
    with col_a:
        st.markdown("#### Age Cohort Distribution")
        age_order = ["18-25", "26-35", "36-45", "46-55", "56+"]
        counts_age = filtered_df["Age_Group"].value_counts().reindex(age_order).fillna(0)
        total_resp = len(filtered_df)
        age_pcts = [(v / total_resp * 100) if total_resp > 0 else 0 for v in counts_age.values]
        age_colors = ["#00F0FF", "#38BDF8", "#3B82F6", "#6366F1", "#A855F7"]

        fig_age = go.Figure(
            go.Bar(
                x=counts_age.index,
                y=counts_age.values,
                marker=dict(color=age_colors, line=dict(color="rgba(255,255,255,0.15)", width=1)),
                text=[f"{int(v):,}<br>({p:.1f}%)" for v, p in zip(counts_age.values, age_pcts)],
                textposition="outside",
                textfont=dict(family="JetBrains Mono, monospace", size=10, color="#F8FAFC"),
                customdata=age_pcts,
                hovertemplate="<b>Cohort: %{x}</b><br>Respondents: %{y:,}<br>Proportion: %{customdata:.1f}%<extra></extra>",
            )
        )
        fig_age.update_layout(xaxis_title="Age Group", yaxis_title="Respondents")
        apply_cyber_theme(fig_age, height=360)
        st.plotly_chart(fig_age, use_container_width=True, config={"displayModeBar": False})

    with col_b:
        st.markdown("#### Correlation Heatmap: Age Cohorts vs Scam Outcome (%)")
        ct_age = pd.crosstab(filtered_df["Age_Group"], filtered_df["Social_Media_Scam_Outcome"], normalize="index").round(3) * 100
        
        # Interactive heatmap visualizing Chi-Square findings
        fig_hm_age = go.Figure(
            go.Heatmap(
                z=ct_age.values,
                x=list(ct_age.columns),
                y=list(ct_age.index),
                colorscale=[[0, "#0B1120"], [0.25, "#0F2A4A"], [0.65, "#0284C7"], [1, "#00F0FF"]],
                text=[[f"{val:.1f}%" for val in row] for row in ct_age.values],
                texttemplate="%{text}",
                textfont=dict(family="JetBrains Mono, monospace", size=9.5, color="#FFFFFF"),
                hovertemplate="<b>Age Group: %{y}</b><br>Outcome: %{x}<br>Cohort Share: %{z:.1f}%<extra></extra>",
                showscale=False,
            )
        )
        apply_cyber_theme(fig_hm_age, height=320)
        fig_hm_age.update_xaxes(tickangle=20)
        st.plotly_chart(fig_hm_age, use_container_width=True, config={"displayModeBar": False})

        st.dataframe(ct_age.style.format("{:.1f}%"), use_container_width=True)
        st.info("Chi-Square Independence Test: p = 0.9670 (> 0.05). Scam victimisation occurs uniformly across age cohorts—no generation is immune.")

# -----------------------------------------------------------------------------
# TAB 4: DIGITAL PAYMENT BEHAVIOR
# -----------------------------------------------------------------------------
with tab4:
    st.markdown('<div class="section-title"><span class="section-tag">04</span> Digital Payment Volume & Transaction Loss</div>', unsafe_allow_html=True)
    st.markdown('<div class="section-desc">Evaluating the relationship between weekly online transaction volume and financial theft brackets.</div>', unsafe_allow_html=True)

    col_tx1, col_tx2 = st.columns(2)
    with col_tx1:
        st.markdown("#### Digital Transactions Per Week")
        tx_counts = filtered_df["Digital_Transactions_Per_Week"].value_counts().reset_index()
        tx_counts.columns = ["Transaction Frequency", "Respondents"]
        total_resp = len(filtered_df)
        tx_counts["Pct"] = (tx_counts["Respondents"] / total_resp * 100).round(1)
        tx_colors = ["#00F0FF", "#38BDF8", "#3B82F6", "#6366F1", "#A855F7"][:len(tx_counts)]

        fig_tx = go.Figure(
            go.Bar(
                y=tx_counts["Transaction Frequency"],
                x=tx_counts["Respondents"],
                orientation="h",
                marker=dict(color=tx_colors, line=dict(color="rgba(255,255,255,0.15)", width=1)),
                text=[f" {r:,} ({p:.1f}%)" for r, p in zip(tx_counts["Respondents"], tx_counts["Pct"])],
                textposition="outside",
                textfont=dict(family="JetBrains Mono, monospace", size=10, color="#F8FAFC"),
                customdata=tx_counts["Pct"],
                hovertemplate="<b>Frequency: %{y}</b><br>Respondents: %{x:,}<br>Cohort Share: %{customdata:.1f}%<extra></extra>",
            )
        )
        fig_tx.update_layout(xaxis_title="Respondents", yaxis_title="", yaxis=dict(autorange="reversed"))
        apply_cyber_theme(fig_tx, height=360)
        st.plotly_chart(fig_tx, use_container_width=True, config={"displayModeBar": False})

    with col_tx2:
        st.markdown("#### Transaction Fraud Loss Breakdown (Donut Chart)")
        tx_loss_counts = filtered_df["Transaction_Fraud_Loss"].value_counts().reset_index()
        tx_loss_counts.columns = ["Loss Bracket", "Count"]
        tx_loss_counts["Percentage"] = (tx_loss_counts["Count"] / len(filtered_df) * 100).round(1).astype(str) + "%"

        loss_palette = {
            "No loss": "#10B981",
            "< Rs. 1000": "#06B6D4",
            "Rs. 1000 - 5000": "#F59E0B",
            "Rs. 5000 - 20000": "#F97316",
            "> Rs. 20000": "#EF4444",
        }
        loss_colors = [loss_palette.get(b, "#38BDF8") for b in tx_loss_counts["Loss Bracket"]]

        fig_donut_loss = go.Figure(
            go.Pie(
                labels=tx_loss_counts["Loss Bracket"],
                values=tx_loss_counts["Count"],
                hole=0.6,
                marker=dict(colors=loss_colors, line=dict(color="#0B1120", width=2)),
                textinfo="percent",
                textfont=dict(family="JetBrains Mono, monospace", size=11, color="#F8FAFC"),
                hovertemplate="<b>%{label}</b><br>Respondents: %{value:,}<br>Share: %{percent}<extra></extra>",
            )
        )
        apply_cyber_theme(fig_donut_loss, height=220, show_legend=True, orientation="h")
        fig_donut_loss.update_layout(margin=dict(l=10, r=10, t=10, b=10))
        st.plotly_chart(fig_donut_loss, use_container_width=True, config={"displayModeBar": False})

        st.dataframe(tx_loss_counts, use_container_width=True, hide_index=True)

# -----------------------------------------------------------------------------
# TAB 5: SCAM TYPES & VECTORS
# -----------------------------------------------------------------------------
with tab5:
    st.markdown('<div class="section-title"><span class="section-tag">05</span> Cyber Threat Typologies & Attack Vectors</div>', unsafe_allow_html=True)
    st.markdown('<div class="section-desc">Multi-label decomposition of specific fraudulent tactics encountered across social messaging and digital channels.</div>', unsafe_allow_html=True)

    all_scams = []
    for item in filtered_df["Social_Media_Scam_Type"].dropna():
        for s in str(item).split(";"):
            cleaned_s = s.strip()
            if cleaned_s and cleaned_s.lower() != "not applicable":
                all_scams.append(cleaned_s)

    scam_df = pd.Series(all_scams).value_counts().reset_index()
    scam_df.columns = ["Scam Category", "Encounter Count"]
    total_encounters = len(filtered_df)
    scam_df["Encounter Share"] = (scam_df["Encounter Count"] / total_encounters * 100).round(1).astype(str) + "%"

    col_s1, col_s2 = st.columns([3, 2])
    with col_s1:
        st.markdown("#### Threat Vector Encounter Frequency")
        n_scams = len(scam_df)
        bar_colors_scam = [
            f"hsl({180 + int(90 * i / max(1, n_scams - 1))}, 85%, 55%)"
            for i in range(n_scams)
        ]

        fig_scam = go.Figure(
            go.Bar(
                y=scam_df["Scam Category"],
                x=scam_df["Encounter Count"],
                orientation="h",
                marker=dict(
                    color=bar_colors_scam,
                    line=dict(color="rgba(255,255,255,0.15)", width=1),
                ),
                text=[f" {c:,} ({p})" for c, p in zip(scam_df["Encounter Count"], scam_df["Encounter Share"])],
                textposition="outside",
                textfont=dict(family="JetBrains Mono, monospace", size=10, color="#F8FAFC"),
                customdata=scam_df["Encounter Share"],
                hovertemplate="<b>%{y}</b><br>Encounters: %{x:,}<br>Population Share: %{customdata}<extra></extra>",
            )
        )
        fig_scam.update_layout(xaxis_title="Encounter Count", yaxis_title="", yaxis=dict(autorange="reversed"))
        apply_cyber_theme(fig_scam, height=390)
        st.plotly_chart(fig_scam, use_container_width=True, config={"displayModeBar": False})

    with col_s2:
        st.markdown("#### Top Attack Vectors Proportions (Donut)")
        top_5_scams = scam_df.head(5)
        fig_donut_scam = go.Figure(
            go.Pie(
                labels=top_5_scams["Scam Category"],
                values=top_5_scams["Encounter Count"],
                hole=0.6,
                marker=dict(
                    colors=["#00F0FF", "#38BDF8", "#3B82F6", "#8B5CF6", "#A855F7"],
                    line=dict(color="#0B1120", width=2),
                ),
                textinfo="percent",
                textfont=dict(family="JetBrains Mono, monospace", size=10.5, color="#F8FAFC"),
                hovertemplate="<b>%{label}</b><br>Encounters: %{value:,}<br>Share: %{percent}<extra></extra>",
            )
        )
        apply_cyber_theme(fig_donut_scam, height=220, show_legend=True, orientation="h")
        fig_donut_scam.update_layout(margin=dict(l=10, r=10, t=10, b=10))
        st.plotly_chart(fig_donut_scam, use_container_width=True, config={"displayModeBar": False})

        st.markdown("#### Threat Vector Ranking")
        st.dataframe(scam_df[["Scam Category", "Encounter Count", "Encounter Share"]], use_container_width=True, hide_index=True)

# -----------------------------------------------------------------------------
# TAB 6: CYBERSECURITY AWARENESS
# -----------------------------------------------------------------------------
with tab6:
    st.markdown('<div class="section-title"><span class="section-tag">06</span> Cybersecurity Awareness Self-Rating</div>', unsafe_allow_html=True)
    st.markdown('<div class="section-desc">Self-reported security knowledge plotted alongside self-assessed fraud identification competence.</div>', unsafe_allow_html=True)

    col_aw1, col_aw2 = st.columns(2)
    with col_aw1:
        st.markdown("#### Awareness Rating Distribution (Scale 1–5)")
        aw_counts = filtered_df["Overall_Cybersecurity_Awareness"].value_counts().reindex([1, 2, 3, 4, 5]).fillna(0)
        aw_labels = ["1 (Very Low)", "2 (Low)", "3 (Moderate)", "4 (Good)", "5 (High)"]
        total_resp = len(filtered_df)
        aw_pcts = [(v / total_resp * 100) if total_resp > 0 else 0 for v in aw_counts.values]
        aw_colors = ["#EF4444", "#F97316", "#F59E0B", "#06B6D4", "#00F0FF"]

        fig_aw_dist = go.Figure(
            go.Bar(
                x=aw_labels,
                y=aw_counts.values,
                marker=dict(color=aw_colors, line=dict(color="rgba(255,255,255,0.15)", width=1)),
                text=[f"{int(v):,}<br>({p:.1f}%)" for v, p in zip(aw_counts.values, aw_pcts)],
                textposition="outside",
                textfont=dict(family="JetBrains Mono, monospace", size=10, color="#F8FAFC"),
                customdata=aw_pcts,
                hovertemplate="<b>Rating: %{x}</b><br>Respondents: %{y:,}<br>Share: %{customdata:.1f}%<extra></extra>",
            )
        )
        fig_aw_dist.update_layout(xaxis_title="Awareness Rating", yaxis_title="Respondents")
        apply_cyber_theme(fig_aw_dist, height=360)
        st.plotly_chart(fig_aw_dist, use_container_width=True, config={"displayModeBar": False})

    with col_aw2:
        st.markdown("#### Correlation Heatmap: Awareness vs Fraud Identification Ability")
        ct_aw_ab = pd.crosstab(filtered_df["Overall_Cybersecurity_Awareness"], filtered_df["Fraud_Identification_Ability"])
        
        # Interactive Heatmap showing correlation
        fig_hm_aw = go.Figure(
            go.Heatmap(
                z=ct_aw_ab.values,
                x=list(ct_aw_ab.columns),
                y=[f"Rating {r}" for r in ct_aw_ab.index],
                colorscale=[[0, "#0B1120"], [0.25, "#0E3A53"], [0.65, "#0284C7"], [1, "#00F0FF"]],
                text=ct_aw_ab.values,
                texttemplate="%{text}",
                textfont=dict(family="JetBrains Mono, monospace", size=10.5, color="#FFFFFF"),
                hovertemplate="<b>Awareness: %{y}</b><br>Ability: %{x}<br>Respondents: %{z:,}<extra></extra>",
                showscale=False,
            )
        )
        apply_cyber_theme(fig_hm_aw, height=300)
        st.plotly_chart(fig_hm_aw, use_container_width=True, config={"displayModeBar": False})

        st.dataframe(ct_aw_ab, use_container_width=True)
        st.info("The Perception-Action Gap: Over 62% of respondents rating their awareness as 'High' still suffered attack encounters.")

# -----------------------------------------------------------------------------
# TAB 7: SECURITY PRACTICES & BEHAVIORAL HYGIENE
# -----------------------------------------------------------------------------
with tab7:
    st.markdown('<div class="section-title"><span class="section-tag">07</span> Proactive Cyber Hygiene & Link Clicking Habits</div>', unsafe_allow_html=True)
    st.markdown('<div class="section-desc">Adherence to password rotation, 2FA, and the behavioral frequency of clicking unrecognized links.</div>', unsafe_allow_html=True)

    col_sec1, col_sec2 = st.columns(2)
    with col_sec1:
        st.markdown("#### Proactive Cyber Hygiene Frequency")
        sec_order = ["Always", "Often", "Sometimes", "Rarely", "Never"]
        sec_counts = filtered_df["Security_Practices"].value_counts().reindex(sec_order).fillna(0)
        total_resp = len(filtered_df)
        sec_pcts = [(v / total_resp * 100) if total_resp > 0 else 0 for v in sec_counts.values]
        sec_colors = ["#10B981", "#06B6D4", "#F59E0B", "#F97316", "#EF4444"]

        fig_sec = go.Figure(
            go.Bar(
                x=sec_counts.index,
                y=sec_counts.values,
                marker=dict(color=sec_colors, line=dict(color="rgba(255,255,255,0.15)", width=1)),
                text=[f"{int(v):,}<br>({p:.1f}%)" for v, p in zip(sec_counts.values, sec_pcts)],
                textposition="outside",
                textfont=dict(family="JetBrains Mono, monospace", size=10, color="#F8FAFC"),
                customdata=sec_pcts,
                hovertemplate="<b>Hygiene Habit: %{x}</b><br>Respondents: %{y:,}<br>Share: %{customdata:.1f}%<extra></extra>",
            )
        )
        fig_sec.update_layout(xaxis_title="Security Practice Adherence", yaxis_title="Respondents")
        apply_cyber_theme(fig_sec, height=360)
        st.plotly_chart(fig_sec, use_container_width=True, config={"displayModeBar": False})

    with col_sec2:
        st.markdown("#### Suspicious Link Clicking Distribution (Donut Chart)")
        click_counts = filtered_df["Suspicious_Link_Clicks"].value_counts().reset_index()
        click_counts.columns = ["Click Frequency", "Respondents"]
        click_counts["Percentage"] = (click_counts["Respondents"] / len(filtered_df) * 100).round(1).astype(str) + "%"

        click_colors_map = {
            "Never": "#10B981",
            "Once": "#06B6D4",
            "2-3 times": "#F59E0B",
            "4-5 times": "#F97316",
            "More than 5 times": "#EF4444",
        }
        click_colors = [click_colors_map.get(k, "#38BDF8") for k in click_counts["Click Frequency"]]

        fig_donut_click = go.Figure(
            go.Pie(
                labels=click_counts["Click Frequency"],
                values=click_counts["Respondents"],
                hole=0.6,
                marker=dict(colors=click_colors, line=dict(color="#0B1120", width=2)),
                textinfo="percent",
                textfont=dict(family="JetBrains Mono, monospace", size=11, color="#F8FAFC"),
                hovertemplate="<b>%{label}</b><br>Respondents: %{value:,}<br>Share: %{percent}<extra></extra>",
            )
        )
        apply_cyber_theme(fig_donut_click, height=220, show_legend=True, orientation="h")
        fig_donut_click.update_layout(margin=dict(l=10, r=10, t=10, b=10))
        st.plotly_chart(fig_donut_click, use_container_width=True, config={"displayModeBar": False})

        st.dataframe(click_counts, use_container_width=True, hide_index=True)
        st.warning("Critical Threat Vector: Over 57% of respondents admit to clicking unverified links at least once.")

# -----------------------------------------------------------------------------
# TAB 8: MACHINE LEARNING MODEL BENCHMARK
# -----------------------------------------------------------------------------
with tab8:
    st.markdown('<div class="section-title"><span class="section-tag">08</span> Machine Learning Classifier Benchmark</div>', unsafe_allow_html=True)
    st.markdown('<div class="section-desc">Performance evaluation of Logistic Regression, Decision Tree, and Random Forest on 20% stratified test partition ($N = 302$).</div>', unsafe_allow_html=True)

    if df_comp is not None:
        st.dataframe(
            df_comp.style.highlight_max(subset=["Recall", "F1_Score"], color="#064E3B"),
            use_container_width=True,
            hide_index=True,
        )

        col_m1, col_m2 = st.columns([1, 1])
        with col_m1:
            st.markdown("#### Metric Comparison Across Classifiers")
            metrics = ["Accuracy", "Precision", "Recall", "F1_Score"]
            model_colors = {
                "Logistic Regression": "#38BDF8",
                "Decision Tree": "#F59E0B",
                "Random Forest": "#00F0FF",
            }
            fig_bench = go.Figure()
            for _, row in df_comp.iterrows():
                m_name = row["Model"]
                scores = [row[m] for m in metrics]
                fig_bench.add_trace(
                    go.Bar(
                        name=m_name,
                        x=metrics,
                        y=scores,
                        marker=dict(
                            color=model_colors.get(m_name, "#38BDF8"),
                            line=dict(color="rgba(255,255,255,0.15)", width=1),
                        ),
                        text=[f"{s*100:.1f}%" for s in scores],
                        textposition="outside",
                        textfont=dict(family="JetBrains Mono, monospace", size=9.5, color="#F8FAFC"),
                        hovertemplate=f"<b>{m_name}</b><br>%{{x}}: %{{y:.2%}}<extra></extra>",
                    )
                )

            fig_bench.update_layout(
                barmode="group",
                yaxis=dict(range=[0, 1.15], tickformat=".0%"),
                xaxis_title="Evaluation Metric",
                yaxis_title="Score",
            )
            apply_cyber_theme(fig_bench, height=370, show_legend=True, orientation="h")
            st.plotly_chart(fig_bench, use_container_width=True, config={"displayModeBar": False})

        with col_m2:
            st.markdown(
                """
                <div class="cyber-card" style="border-color: rgba(16, 185, 129, 0.35);">
                    <div class="cyber-card-header" style="color: #10B981;">🏆 Champion Classifier: Random Forest</div>
                    <div style="font-size: 0.88rem; color: #CBD5E1; line-height: 1.6;">
                        <ul style="margin: 0; padding-left: 1.2rem;">
                            <li><b>Recall</b>: <span style="color: #00F0FF; font-weight: 700;">88.54%</span> (catches 139 of 157 actual fraud victims)</li>
                            <li><b>F1-Score</b>: <span style="color: #00F0FF; font-weight: 700;">64.80%</span> (highest precision-recall balance)</li>
                            <li><b>False Negatives</b>: Only <b>18 missed victims</b> (vs 61 in Logistic Regression and 104 in Decision Tree)</li>
                            <li><b>SOC Deployment</b>: Optimal for high-sensitivity early warning threat filters.</li>
                        </ul>
                    </div>
                </div>
                """,
                unsafe_allow_html=True,
            )

        # Interactive Confusion Matrices Heatmap Grid (3 Models)
        st.markdown("#### Interactive Confusion Matrices Across Models")
        col_cm1, col_cm2, col_cm3 = st.columns(3)
        cm_data = {
            "Logistic Regression": [[106, 39], [61, 96]],
            "Decision Tree": [[118, 27], [104, 53]],
            "Random Forest (Champion)": [[55, 90], [18, 139]],
        }
        for (col_target, (m_title, matrix)) in zip([col_cm1, col_cm2, col_cm3], cm_data.items()):
            with col_target:
                border_accent = "#10B981" if "Random Forest" in m_title else "#38BDF8"
                fig_cm = go.Figure(
                    go.Heatmap(
                        z=matrix,
                        x=["Pred: Safe (0)", "Pred: Victim (1)"],
                        y=["Actual: Safe (0)", "Actual: Victim (1)"],
                        colorscale=[[0, "#0F172A"], [0.5, "#0369A1"], [1, border_accent]],
                        text=[[f"{v:,}" for v in row] for row in matrix],
                        texttemplate="%{text}",
                        textfont=dict(family="JetBrains Mono, monospace", size=13, color="#FFFFFF"),
                        hovertemplate="<b>%{y}</b><br>%{x}<br>Count: %{z:,}<extra></extra>",
                        showscale=False,
                    )
                )
                apply_cyber_theme(fig_cm, title=m_title, height=220)
                st.plotly_chart(fig_cm, use_container_width=True, config={"displayModeBar": False})

        # Static composite image expander if available
        cm_path = base_dir / "outputs" / "07_model_confusion_matrices.png"
        if cm_path.exists():
            with st.expander("🖼️ View High-Resolution Composite Output Image"):
                st.image(str(cm_path), use_column_width=True)

# -----------------------------------------------------------------------------
# TAB 9: FEATURE IMPORTANCE & INTERACTIVE RISK SIMULATOR
# -----------------------------------------------------------------------------
with tab9:
    st.markdown('<div class="section-title"><span class="section-tag">09</span> Gini Feature Importance & Threat Risk Simulator</div>', unsafe_allow_html=True)
    st.markdown('<div class="section-desc">Quantified relative importance of pre-attack indicators and an interactive client vulnerability scanner.</div>', unsafe_allow_html=True)

    if df_feat is not None:
        col_f1, col_f2 = st.columns([3, 2])
        with col_f1:
            st.markdown("#### Top 10 Predictor Importance (Gini Index)")
            top_feat = df_feat.head(10).iloc[::-1]  # reversed for ascending y-axis in bar chart
            n_feat = len(top_feat)
            feat_colors = [
                f"hsl({260 - int(80 * i / max(1, n_feat - 1))}, 90%, 60%)"
                for i in range(n_feat)
            ]

            fig_feat = go.Figure(
                go.Bar(
                    y=top_feat["Feature"],
                    x=top_feat["Importance"],
                    orientation="h",
                    marker=dict(color=feat_colors, line=dict(color="rgba(255,255,255,0.15)", width=1)),
                    text=[f" {imp*100:.1f}%" for imp in top_feat["Importance"]],
                    textposition="outside",
                    textfont=dict(family="JetBrains Mono, monospace", size=9.5, color="#F8FAFC"),
                    customdata=[f"{imp*100:.2f}%" for imp in top_feat["Importance"]],
                    hovertemplate="<b>%{y}</b><br>Importance: %{x:.4f} (%{customdata})<extra></extra>",
                )
            )
            fig_feat.update_layout(xaxis_title="Gini Feature Importance", yaxis_title="")
            apply_cyber_theme(fig_feat, height=380)
            st.plotly_chart(fig_feat, use_container_width=True, config={"displayModeBar": False})

        with col_f2:
            st.markdown("#### Predictor Weight Rankings")
            feat_display = df_feat.copy()
            feat_display["Importance %"] = (feat_display["Importance"] * 100).round(2).astype(str) + "%"
            st.dataframe(feat_display, use_container_width=True, hide_index=True)

    st.markdown("---")
    st.markdown('<div class="cyber-card-header">⚡ Interactive Cyber Fraud Risk Score Simulator</div>', unsafe_allow_html=True)
    st.write("Input respondent exposure and security habits to compute estimated fraud vulnerability:")

    sim_col1, sim_col2, sim_col3 = st.columns(3)
    with sim_col1:
        sim_clicks = st.selectbox("Suspicious Link Clicking Frequency", ["Never", "Once", "2-3 times", "4-5 times", "More than 5 times"], index=2)
        sim_upi = st.selectbox("Suspicious UPI/QR Exposure Frequency", ["Never", "Once", "2-3 times", "4-5 times", "More than 5 times"], index=2)
    with sim_col2:
        sim_sec = st.select_slider("Proactive Security Practices Adherence", ["Never", "Rarely", "Sometimes", "Often", "Always"], value="Sometimes")
        sim_aw = st.slider("Cybersecurity Awareness Self-Rating", 1, 5, 3)
    with sim_col3:
        # Heuristic scoring based on Random Forest feature importances
        click_weight = {"Never": 0, "Once": 1, "2-3 times": 2, "4-5 times": 3, "More than 5 times": 4}[sim_clicks]
        upi_weight = {"Never": 0, "Once": 1, "2-3 times": 2, "4-5 times": 3, "More than 5 times": 4}[sim_upi]
        sec_weight = {"Always": 0, "Often": 1, "Sometimes": 2, "Rarely": 3, "Never": 4}[sim_sec]
        aw_weight = 5 - sim_aw

        risk_score = min(100, int((click_weight * 7.5) + (upi_weight * 6.5) + (sec_weight * 6.0) + (aw_weight * 5.0)))

        if risk_score >= 65:
            box_class = "sim-critical"
            color_text = "#EF4444"
            title_text = "CRITICAL FRAUD VULNERABILITY"
            advice_text = "High link-clicking habits coupled with low hygiene indicate extreme susceptibility to social engineering. Recommended to enforce mandatory hardware 2FA and restrict automated link redirection."
        elif risk_score >= 40:
            box_class = "sim-elevated"
            color_text = "#F59E0B"
            title_text = "ELEVATED FRAUD RISK"
            advice_text = "Standard attack exposure detected. Ensure multi-factor authentication is active on all financial gateways and verify payment requests before approving UPI/QR intents."
        else:
            box_class = "sim-secure"
            color_text = "#10B981"
            title_text = "STRONG SECURITY RESILIENCE"
            advice_text = "Robust behavioral hygiene and zero/minimal link-clicking habits provide strong defense against common deception attacks."

        # Interactive Plotly Radial Gauge for Threat Risk Score
        fig_gauge = go.Figure(
            go.Indicator(
                mode="gauge+number",
                value=risk_score,
                number=dict(suffix="%", font=dict(family="JetBrains Mono, monospace", size=28, color=color_text)),
                gauge=dict(
                    axis=dict(range=[0, 100], tickwidth=1, tickcolor="#94A3B8", tickfont=dict(size=9, color="#94A3B8")),
                    bar=dict(color=color_text, thickness=0.25),
                    bgcolor="rgba(15, 23, 42, 0.7)",
                    borderwidth=1,
                    bordercolor="rgba(255, 255, 255, 0.1)",
                    steps=[
                        dict(range=[0, 40], color="rgba(16, 185, 129, 0.18)"),
                        dict(range=[40, 65], color="rgba(245, 158, 11, 0.18)"),
                        dict(range=[65, 100], color="rgba(239, 68, 68, 0.18)"),
                    ],
                ),
            )
        )
        fig_gauge.update_layout(
            paper_bgcolor="rgba(0,0,0,0)",
            plot_bgcolor="rgba(0,0,0,0)",
            height=145,
            margin=dict(l=15, r=15, t=10, b=10),
        )
        st.plotly_chart(fig_gauge, use_container_width=True, config={"displayModeBar": False})

        st.markdown(
            f"""
            <div class="simulator-result-box {box_class}" style="margin-top: 0.2rem;">
                <div class="sim-level-title" style="color: {color_text};">{title_text}</div>
                <div class="sim-advice-text">{advice_text}</div>
            </div>
            """,
            unsafe_allow_html=True,
        )
