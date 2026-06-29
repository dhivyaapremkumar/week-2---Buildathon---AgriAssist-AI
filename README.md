# 🌾 AgriAssist AI

## AI-Powered Agricultural Scheme Information System

AgriAssist AI is an intelligent Retrieval-Augmented Generation (RAG) application that helps farmers and citizens easily explore Tamil Nadu Government Agricultural Schemes through natural language conversations.

Instead of manually searching government websites, users can ask questions such as:

* What seed subsidy schemes are available?
* How can I apply for farmer training?
* Who is eligible for Gypsum subsidy?

The application retrieves relevant government scheme information using a hybrid retrieval pipeline and generates accurate, context-aware answers using OpenAI GPT.

---

# Features

* 🌾 Tamil Nadu Government Agriculture Scheme Explorer
* 🤖 AI-powered conversational assistant
* 🔍 Hybrid Retrieval (Keyword Search + FAISS Vector Search)
* 📚 LangChain-based RAG Pipeline
* 🧠 OpenAI GPT Integration
* 📄 PDF download for scheme details
* 📊 Interactive Dashboard
* 🔐 Secure API key management using `.env`
* 🎨 Professional Streamlit Interface
* 📁 Structured JSON Knowledge Base

---

# System Architecture

```
Tamil Nadu Government Website
            │
            ▼
       Web Scraper
            │
            ▼
      Structured JSON
            │
     OpenAI Embeddings
            │
            ▼
       FAISS Vector DB
            │
            ▼
   LangChain Retriever
            │
            ▼
        OpenAI GPT
            │
            ▼
    Streamlit Dashboard
```

---

# Technology Stack

| Layer           | Technology               |
| --------------- | ------------------------ |
| Frontend        | Streamlit                |
| Backend         | Python 3.14              |
| LLM             | OpenAI GPT               |
| Framework       | LangChain                |
| Embeddings      | text-embedding-3-small   |
| Vector Database | FAISS                    |
| Observability   | LangSmith                |
| Web Scraping    | Requests + BeautifulSoup |
| PDF Generation  | ReportLab                |

---

# Project Structure

```
TN_Agriculture_AI/

├── app.py
├── .env
├── requirements.txt
│
├── config/
├── scraper/
├── data/
├── vectorstore/
├── llm/
├── ui/
├── db/
```

---

# Installation

## Clone Repository

```bash
git clone <repository-url>
cd TN_Agriculture_AI
```

## Create Virtual Environment

```bash
python -m venv venv
```

Activate the environment.

Windows

```bash
venv\Scripts\activate
```

Linux / macOS

```bash
source venv/bin/activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Configure Environment Variables

Create a `.env` file.

```
OPENAI_API_KEY=your_openai_api_key

LANGCHAIN_API_KEY=your_langsmith_key

LANGCHAIN_TRACING_V2=true

LANGCHAIN_PROJECT=AgriAssist_AI
```

---

## Build Vector Database

```bash
python vectorstore/create_vectorstore.py
```

---

## Run Application

```bash
streamlit run app.py
```

---

# Workflow

1. Scrape Tamil Nadu Government Agriculture schemes.
2. Parse structured information.
3. Clean and normalize data.
4. Store as JSON.
5. Generate embeddings using OpenAI.
6. Store vectors in FAISS.
7. Retrieve relevant schemes using Hybrid Retrieval.
8. Generate AI response using GPT.
9. Display results in Streamlit.
10. Included chatbot interaction in both english and tamil
---

# Future Enhancements

* Voice-based interaction
* Farmer login and saved history
* Scheme recommendation engine
* OCR support for uploaded documents
* Mobile application

---

# Author

**Dhivyaa Premkumar**

Buildathon Project – AgriAssist AI
