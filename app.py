import streamlit as st
from ui.styles import load_css
from ui.sidebar import sidebar
from ui.header import show_header
from ui.dashboard import show_dashboard
from ui.cards import show_scheme_card
from ui.chat import chat_interface
st.set_page_config(
    page_title="AgriAssist AI",
    page_icon="🌾",
    layout="wide",
    initial_sidebar_state="expanded"
)

load_css()

selected_scheme, schemes = sidebar()
show_header()
show_dashboard()
left, right = st.columns([1, 2])
with left:

    st.markdown(
        '<p class="main-title">🌾 AgriAssist AI</p>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<p class="subtitle">Tamil Nadu Agricultural Scheme Assistant</p>',
        unsafe_allow_html=True
    )

    show_scheme_card(
        selected_scheme,
        schemes
    )

with right:

    chat_interface()