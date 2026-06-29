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

def chat_interface(farmer_type, language, district):

    initialize_chat()

    chatbot = load_chatbot()

    st.markdown("## 💬 AI Assistant")

    display_chat()

    st.markdown("### 💡 Suggested Questions")

    col1, col2, col3 = st.columns(3)

    question = None


    if col1.button("🌾 Paddy Farmer"):
       question = (
        "I cultivate paddy. "
        "Which government schemes can help me?"
    )

    elif col2.button("🌱 Seed Subsidy"):
       question = (
        "I need certified seeds. "
        "Which subsidy schemes are available?"
    )

    elif col3.button("🚜 Farm Equipment"):
       question = (
        "Are there any government schemes "
        "for purchasing agricultural equipment?"
    )

    else:
       question = st.chat_input(
        "Describe your farming need..."
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
            def detect_intent(question):

              q = question.lower()

              if any(word in q for word in ["seed", "விதை"]):
                return "Seed Subsidy"

              elif any(word in q for word in [
        "training", "பயிற்சி"
    ]):
                 return "Farmer Training"

              elif any(word in q for word in [
        "equipment", "tractor", "implement",
        "கருவி", "டிராக்டர்"
    ]):
                  return "Farm Equipment"

              elif any(word in q for word in [
        "irrigation", "drip", "sprinkler",
        "நீர்ப்பாசனம்"
    ]):
                  return "Irrigation"

              elif any(word in q for word in [
        "organic", "இயற்கை"
    ]):
                   return "Organic Farming"

              elif any(word in q for word in [
        "woman", "women", "பெண்"
    ]):
                    return "Women Farmer"

              elif any(word in q for word in [
        "maize", "மக்காச்சோளம்"
    ]):
                    return "Maize Cultivation"

              elif any(word in q for word in [
        "paddy", "rice", "நெல்"
    ]):
                    return "Paddy Cultivation"

              return "General Agriculture"
            intent = detect_intent(question)
            enhanced_question = f"""Language: {language}Farmer Category: {farmer_type}District: {district}Farmer Intent:
{intent} Question:{question}"""
            
            result = chatbot.ask(enhanced_question)
            

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