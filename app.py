import os
import tempfile
import streamlit as st
from dotenv import load_dotenv
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings
from langchain_openai import ChatOpenAI

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

st.set_page_config(page_title="PDF RAG App")

st.title("📄 PDF Question Answering")

uploaded_file = st.file_uploader(
    "Upload a PDF",
    type="pdf"
)

if "vectorstore" not in st.session_state:
    st.session_state.vectorstore = None

if uploaded_file:

    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
        tmp.write(uploaded_file.read())
        pdf_path = tmp.name

    with st.spinner("Loading PDF..."):
        loader = PyPDFLoader(pdf_path)
        documents = loader.load()

    with st.spinner("Splitting text..."):
        splitter = RecursiveCharacterTextSplitter(
            chunk_size=1000,
            chunk_overlap=200
        )

        chunks = splitter.split_documents(documents)

    with st.spinner("Creating embeddings..."):
        
        embeddings = OpenAIEmbeddings(
            model="text-embedding-3-small",
            api_key=OPENAI_API_KEY
        )
        vectorstore = FAISS.from_documents(
            chunks,
            embeddings
        )

        st.session_state.vectorstore = vectorstore

    st.success("PDF processed successfully.")

question = st.text_input(
    "Ask a question about the PDF"
)

if question and st.session_state.vectorstore:

    retriever = st.session_state.vectorstore.as_retriever(
        search_kwargs={"k": 4}
    )

    docs = retriever.invoke(question)

    context = "\n\n".join(
        [doc.page_content for doc in docs]
    )

    prompt = f"""
Answer the question using only the context below.

Context:
{context}

Question:
{question}

Answer:
"""

    llm = ChatOpenAI(
        model="gpt-4o-mini",
        api_key=OPENAI_API_KEY,
        temperature=0
    )

    response = llm.invoke(prompt)

    st.subheader("Answer")
    st.write(response.content)