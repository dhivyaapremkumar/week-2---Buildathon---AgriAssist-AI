"""
=========================================================
File : sidebar.py
Purpose : Sidebar UI
=========================================================
"""

import json
from pathlib import Path

import streamlit as st

PROJECT_ROOT = Path(__file__).resolve().parent.parent
DATA_FILE = PROJECT_ROOT / "data" / "schemes.json"


def load_schemes():
    try:
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception as e:
        st.error(f"Unable to load schemes.json\n\n{e}")
        return []


def sidebar():

    schemes = load_schemes()

    # -----------------------------
    # Sidebar Header
    # -----------------------------
    with st.sidebar:

        st.markdown("# 🌾 AgriAssist AI")
        st.caption("Tamil Nadu Agriculture Scheme Assistant")

        st.divider()

        st.metric(
            "📄 Total Schemes",
            len(schemes)
        )

        st.metric(
            "🤖 AI Engine",
            "GPT + LangChain"
        )

        st.divider()

        search = st.text_input(
            "🔍 Search Scheme"
        )

        scheme_names = sorted([
            s.get("metadata", {}).get("scheme_name", "")
            for s in schemes
            if s.get("metadata", {}).get("scheme_name")
        ])

        if search:
            scheme_names = [
                s for s in scheme_names
                if search.lower() in s.lower()
            ]

        selected = st.selectbox(
            "🌱 Agriculture Schemes",
            ["Select a Scheme"] + scheme_names
        )

        st.divider()

        st.success(
            "Agriculture - Farmers Welfare Department"
        )

        st.caption(
            "Powered by OpenAI • LangChain • FAISS"
        )

    return selected, schemes