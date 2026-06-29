"""
=========================================================
File : chatbot.py
Project : AgriAssist AI

Purpose
-------
Hybrid RAG Chatbot

1. Keyword Search
2. FAISS Retrieval
3. GPT Response

Author : Dhivyaa
=========================================================
"""

from pathlib import Path
import json

from llm.chains import AgricultureChain


# -------------------------------------------------------
# Project Paths
# -------------------------------------------------------

PROJECT_ROOT = Path(__file__).resolve().parent.parent

DATA_FILE = PROJECT_ROOT / "data" / "schemes.json"


# -------------------------------------------------------
# Chatbot
# -------------------------------------------------------

class AgricultureChatbot:

    def __init__(self):

        self.chain_builder = AgricultureChain()

        self.chain = self.chain_builder.build_chain()

        self.retriever = self.chain_builder.retriever

        with open(DATA_FILE, "r", encoding="utf-8") as f:
            self.schemes = json.load(f)

    # ---------------------------------------------------
    # Keyword Search
    # ---------------------------------------------------

    def keyword_search(self, question):

        question = question.lower()

        keywords = [
            "seed",
            "training",
            "subsidy",
            "benefit",
            "beneficiary",
            "eligibility",
            "farmer",
            "maize",
            "paddy",
            "oil",
            "oilseed",
            "gypsum",
            "rhizobium",
            "fertilizer",
            "demonstration",
            "loan"
        ]

        if not any(word in question for word in keywords):
            return []

        matched = []

        for scheme in self.schemes:

            text = scheme["page_content"].lower()

            if any(word in text for word in question.split()):

                matched.append(scheme)

        return matched

    # ---------------------------------------------------
    # Ask
    # ---------------------------------------------------

    def ask(self, question):

        # ===============================================
        # Hybrid Keyword Search
        # ===============================================

        matched = self.keyword_search(question)

        if matched:

            context = "\n\n".join(

                scheme["page_content"]

                for scheme in matched

            )

            answer = self.chain.invoke(
                {
                    "context": context,
                    "question": question
                }
            )

            return {

                "answer": answer,

                "sources": []

            }

        # ===============================================
        # FAISS Retrieval
        # ===============================================

        docs = self.retriever.invoke(question)

        answer = self.chain.invoke(question)

        return {

            "answer": answer,

            "sources": docs

        }