"""
=========================================================
File : dashboard.py
Purpose : Dashboard Statistics
=========================================================
"""

import json
from pathlib import Path
import streamlit as st

PROJECT_ROOT = Path(__file__).resolve().parent.parent

DATA_FILE = PROJECT_ROOT / "data" / "schemes.json"


def load_statistics():

    with open(DATA_FILE, encoding="utf-8") as f:
        schemes = json.load(f)

    total_schemes = len(schemes)

    departments = len(
        set(
            s["metadata"].get("department", "")
            for s in schemes
        )
    )

    beneficiaries = len(
        set(
            s["metadata"].get("beneficiaries", "")
            for s in schemes
        )
    )

    return (
        total_schemes,
        departments,
        beneficiaries
    )


def show_dashboard():

    total, dept, bene = load_statistics()

    st.markdown("## 📊 Agriculture Scheme Dashboard")

    c1, c2, c3, c4 = st.columns(4)

    with c1:
        st.metric(
            "🌾 Total Schemes",
            total
        )

    with c2:
        st.metric(
            "🏛 Departments",
            dept
        )

    with c3:
        st.metric(
            "👨‍🌾 Beneficiary Groups",
            bene
        )

    with c4:
        st.metric(
            "🤖 AI",
            "GPT + LangChain"
        )

    st.divider()