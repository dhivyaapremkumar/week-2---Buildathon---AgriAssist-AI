"""
=========================================
File : retriever.py
Purpose : Load FAISS Retriever
=========================================
"""

from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings

from config.settings import (
    OPENAI_API_KEY,
    FAISS_DB,
    TOP_K,
    FETCH_K,
)


class SchemeRetriever:

    def __init__(self):

        self.embeddings = OpenAIEmbeddings(
            api_key=OPENAI_API_KEY
        )

        self.vectorstore = FAISS.load_local(
            folder_path=str(FAISS_DB),
            embeddings=self.embeddings,
            allow_dangerous_deserialization=True
        )

    def get_retriever(self):

        return self.vectorstore.as_retriever(

                search_type="similarity",
                search_kwargs={"k": 5
            }
        )


if __name__ == "__main__":

    retriever = SchemeRetriever().get_retriever()

    docs = retriever.invoke(
        "Certified Seeds"
    )

    print("=" * 80)

    for doc in docs:

        print(doc.page_content[:500])

        print("-" * 80)