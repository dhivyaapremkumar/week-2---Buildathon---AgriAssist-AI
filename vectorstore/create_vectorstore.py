"""
=========================================================
File : create_vectorstore.py
Project : AgriAssist AI

Purpose
-------
Convert schemes.json into a FAISS vector database
using LangChain and OpenAI Embeddings.

Author : Dhivyaa
=========================================================
"""

from __future__ import annotations

import json
from pathlib import Path

from dotenv import load_dotenv

from langchain_core.documents import Document
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS

# ------------------------------------------------------
# Load Environment Variables
# ------------------------------------------------------

load_dotenv()

# ------------------------------------------------------
# Project Paths
# ------------------------------------------------------

PROJECT_ROOT = Path(__file__).resolve().parent.parent

DATA_FILE = PROJECT_ROOT / "data" / "schemes.json"

DB_FOLDER = PROJECT_ROOT / "db" / "faiss_index"

# ------------------------------------------------------
# Vector Store Builder
# ------------------------------------------------------

class VectorStoreBuilder:

    def __init__(self):

        self.embedding_model = OpenAIEmbeddings(
            model="text-embedding-3-small"
        )

    # --------------------------------------------------

    def load_json(self):

        print("Loading JSON...")

        with open(DATA_FILE, encoding="utf-8") as f:

            data = json.load(f)

        print(f"{len(data)} schemes loaded.")

        return data

    # --------------------------------------------------

    def create_documents(self, data):

        print("Creating LangChain Documents...")

        documents = []

        for item in data:

            doc = Document(

                page_content=item["page_content"],

                metadata=item["metadata"]

            )

            documents.append(doc)

        print(f"{len(documents)} documents created.")

        return documents

    # --------------------------------------------------

    def create_vectorstore(self, documents):

        print("Generating embeddings...")

        vectorstore = FAISS.from_documents(

            documents,

            self.embedding_model

        )

        DB_FOLDER.mkdir(
            parents=True,
            exist_ok=True
        )

        vectorstore.save_local(
            str(DB_FOLDER)
        )

        print("FAISS database created successfully.")

    # --------------------------------------------------

    def build(self):

        data = self.load_json()

        documents = self.create_documents(data)

        self.create_vectorstore(documents)

# ------------------------------------------------------

if __name__ == "__main__":

    builder = VectorStoreBuilder()

    builder.build()