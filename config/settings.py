"""
Project Settings
"""

from pathlib import Path
from dotenv import load_dotenv
import os

load_dotenv()

# Project Root
BASE_DIR = Path(__file__).resolve().parent.parent

# Paths
DATA_DIR = BASE_DIR / "data"
DB_DIR = BASE_DIR / "db"

SCHEME_JSON = DATA_DIR / "schemes.json"
FAISS_DB = DB_DIR / "faiss_index"

# API Keys
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
LANGCHAIN_API_KEY = os.getenv("LANGCHAIN_API_KEY")

# Model
LLM_MODEL = "gpt-4.1-mini"

# Retrieval
TOP_K = 4
FETCH_K = 10