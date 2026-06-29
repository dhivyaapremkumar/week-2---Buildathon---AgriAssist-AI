"""
=========================================
File : styles.py
Purpose : Custom CSS for AgriAssist AI
=========================================
"""

import streamlit as st


def load_css():

    st.markdown(
        """
<style>

/* Hide Streamlit Menu */

#MainMenu {visibility:hidden;}
footer {visibility:hidden;}
header {visibility:hidden;}

/* Main Background */

.stApp{
    background:#F5F8F2;
}

/* Title */

.main-title{
    font-size:42px;
    font-weight:700;
    color:#2E7D32;
}

.subtitle{
    color:#555;
    font-size:18px;
    margin-top:-15px;
}

/* Sidebar */

section[data-testid="stSidebar"]{
    background:#2E7D32;
}

section[data-testid="stSidebar"] *{
    color:black;
}

/* Chat */

.user-msg{

    background:#DCF8C6;

    padding:15px;

    border-radius:12px;

    margin-bottom:10px;

}

.bot-msg{

    background:white;

    padding:15px;

    border-radius:12px;

    border-left:6px solid #2E7D32;

    margin-bottom:15px;

    box-shadow:0px 2px 10px rgba(0,0,0,0.08);

}

/* Buttons */

.stButton>button{

    background:#2E7D32;

    color:white;

    border:none;

    border-radius:10px;

    height:45px;

    width:100%;

    font-weight:bold;

}

.stButton>button:hover{

    background:#388E3C;

}

/* Text Input */

.stTextInput input{

    border-radius:10px;

}

/* Cards */

.card{

background:white;

padding:20px;

border-radius:15px;

box-shadow:0px 3px 12px rgba(0,0,0,0.08);

margin-bottom:15px;

}
/* ===========================
Metric Cards
=========================== */

[data-testid="stMetric"]{

    background:white;

    padding:18px;

    border-radius:15px;

    border:1px solid #E6E6E6;

    box-shadow:0px 4px 15px rgba(0,0,0,.08);

}

/* ===========================
Chat Messages
=========================== */

[data-testid="stChatMessage"]{

    border-radius:15px;

    padding:10px;

    margin-bottom:12px;

}

/* ===========================
Selectbox
=========================== */

.stSelectbox{

    border-radius:10px;

}

/* ===========================
Sidebar Divider
=========================== */

section[data-testid="stSidebar"] hr{

    border:1px solid rgba(255,255,255,.25);

}

/* ===========================
Smooth Animation
=========================== */

*{

    transition:.25s;

}

/* ===========================
Hover Effect
=========================== */

.card:hover{

    transform:translateY(-3px);

    box-shadow:0px 10px 25px rgba(0,0,0,.12);

}

/* ===========================
Success / Warning
=========================== */

.stSuccess{

    border-radius:10px;

}

.stWarning{

    border-radius:10px;

}

.stError{

    border-radius:10px;

}



</style>
""",
        unsafe_allow_html=True,
    )