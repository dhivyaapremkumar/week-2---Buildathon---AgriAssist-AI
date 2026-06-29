"""
=========================================================
File : header.py
Purpose : Buildathon Hero Header
=========================================================
"""

import streamlit as st


def show_header():

    st.markdown(
        """
<div style="
background:linear-gradient(135deg,#1B5E20,#43A047);
padding:35px;
border-radius:18px;
text-align:center;
color:white;
margin-bottom:20px;
">

<h1>🌾 AgriAssist AI</h1>

<h3>
AI-powered Agricultural Scheme Information System
</h3>

<p>
Built using LangChain • OpenAI • FAISS • Streamlit
</p>

</div>
""",
        unsafe_allow_html=True
    )