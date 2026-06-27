"""
=========================================================
File : chains.py
Project : AgriAssist AI

Purpose
-------
LangChain RAG Pipeline

Supports:
1. Automatic FAISS Retrieval
2. Manual Context (Hybrid Search)

Author : Dhivyaa
=========================================================
"""

from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableLambda
from langchain_openai import ChatOpenAI

from config.settings import (
    OPENAI_API_KEY,
    LLM_MODEL
)

from vectorstore.retriever import SchemeRetriever
from llm.prompts import AGRICULTURE_PROMPT


class AgricultureChain:

    def __init__(self):

        self.retriever = SchemeRetriever().get_retriever()

        self.llm = ChatOpenAI(

            api_key=OPENAI_API_KEY,

            model=LLM_MODEL,

            temperature=0

        )

    # -------------------------------------------------

    def format_docs(self, docs):

        return "\n\n".join(

            doc.page_content

            for doc in docs

        )

    # -------------------------------------------------

    def prepare_inputs(self, x):

        # ===========================================
        # Manual Context
        # ===========================================

        if isinstance(x, dict):

            return {

                "context": x["context"],

                "question": x["question"]

            }

        # ===========================================
        # Automatic FAISS Retrieval
        # ===========================================

        docs = self.retriever.invoke(x)

        return {

            "context": self.format_docs(docs),

            "question": x

        }

    # -------------------------------------------------

    def build_chain(self):

        chain = (

            RunnableLambda(self.prepare_inputs)

            | AGRICULTURE_PROMPT

            | self.llm

            | StrOutputParser()

        )

        return chain