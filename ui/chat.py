"""
=========================================
File : chat.py
Purpose : Chat Interface
=========================================
"""

import streamlit as st
from llm.chatbot import AgricultureChatbot


# ---------------------------------
# Load Chatbot (Only Once)
# ---------------------------------

@st.cache_resource
def load_chatbot():
    return AgricultureChatbot()


# ---------------------------------
# Initialize Chat History
# ---------------------------------

def initialize_chat():

    if "messages" not in st.session_state:

        st.session_state.messages = [
            {
                "role": "assistant",
                "content":
                "👋 Hello! I am **AgriAssist AI**.\n\n"
                "Ask me anything about Tamil Nadu Agricultural Schemes."
            }
        ]


# ---------------------------------
# Display Previous Messages
# ---------------------------------

def display_chat():

    for message in st.session_state.messages:

        with st.chat_message(message["role"]):

            st.markdown(message["content"])


# ---------------------------------
# Main Chat UI
# ---------------------------------

def chat_interface():

    initialize_chat()

    chatbot = load_chatbot()

    st.markdown("## 💬 AI Assistant")

    display_chat()

    st.markdown("### 💡 Suggested Questions")

    col1, col2, col3 = st.columns(3)

    question = None

    if col1.button("🌱 Seed Schemes"):
        question = "List all seed related agricultural schemes."

    elif col2.button("🎓 Farmer Training"):
        question = "List all farmer training schemes."

    elif col3.button("💰 Subsidy Schemes"):
        question = "List all subsidy schemes."

    else:
        question = st.chat_input(
            "Ask about any Agriculture Scheme..."
        )

    if not question:
        return

    # ----------------------------
    # User Message
    # ----------------------------

    st.session_state.messages.append(
        {
            "role": "user",
            "content": question
        }
    )

    with st.chat_message("user"):

        st.markdown(question)

    # ----------------------------
    # Assistant Response
    # ----------------------------

    with st.chat_message("assistant"):

        with st.spinner("Searching Agricultural Schemes..."):

            result = chatbot.ask(question)

            answer = result["answer"]

            sources = result["sources"]

            st.markdown(answer)

            st.markdown("---")

            st.markdown("### 📚 Retrieved Schemes")

            if sources:

                for doc in sources:

                    st.success(
                        doc.metadata.get(
                            "scheme_name",
                            "Unknown Scheme"
                        )
                    )

                st.markdown("### 🎯 Confidence")

                if len(sources) >= 3:

                    st.success("🟢 High")

                elif len(sources) == 2:

                    st.warning("🟡 Medium")

                else:

                    st.error("🔴 Low")

            else:

                st.info("No related schemes found.")

    # ----------------------------
    # Save Assistant Message
    # ----------------------------

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": answer
        }
    )