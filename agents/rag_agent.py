import os

from dotenv import load_dotenv
from openai import OpenAI

from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_core.documents import Document
from langchain_openai import OpenAIEmbeddings

# =========================
# LOAD ENV VARIABLES
# =========================

load_dotenv()

api_key = os.getenv("NVIDIA_API_KEY")

# =========================
# NVIDIA CLIENT
# =========================

client = OpenAI(
    base_url="https://integrate.api.nvidia.com/v1",
    api_key=api_key
)

# =========================
# EMBEDDINGS
# =========================

embeddings = OpenAIEmbeddings(
    api_key=api_key
)

# =========================
# VECTOR DATABASE
# =========================

persist_directory = "rag_data"

# =========================
# PROCESS DOCUMENT
# =========================

def process_document(text):

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=50
    )

    chunks = splitter.split_text(text)

    docs = [
        Document(page_content=chunk)
        for chunk in chunks
    ]

    vectordb = Chroma.from_documents(
        docs,
        embeddings,
        persist_directory=persist_directory
    )

    vectordb.persist()

    return vectordb

# =========================
# ASK QUESTIONS
# =========================

def ask_rag_question(question):

    vectordb = Chroma(
        persist_directory=persist_directory,
        embedding_function=embeddings
    )

    retriever = vectordb.as_retriever(
        search_kwargs={"k": 3}
    )

    docs = retriever.get_relevant_documents(question)

    context = "\n\n".join(
        [doc.page_content for doc in docs]
    )

    prompt = f"""
You are an expert cybersecurity AI assistant.

Answer the question using ONLY the provided cybersecurity context.

Context:
{context}

Question:
{question}

Provide a professional and accurate cybersecurity response.
"""

    try:

        response = client.chat.completions.create(
            model="meta/llama-3.1-70b-instruct",
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            temperature=0.2,
            max_tokens=700
        )

        return response.choices[0].message.content

    except Exception as e:

        return f"❌ RAG Error: {str(e)}"
