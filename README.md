# 📄 PDF Question Answering using RAG

A simple **Retrieval-Augmented Generation (RAG)** application built with **Streamlit**, **LangChain**, **FAISS**, and **OpenAI**. 
Upload a PDF and ask questions about its content using GPT-4o Mini.

---

## 🚀 Features

* Upload PDF documents
* Extract text from PDFs
* Split text into manageable chunks
* Generate vector embeddings using OpenAI Embeddings
* Store embeddings in a FAISS vector database
* Retrieve the most relevant document chunks
* Generate accurate answers using GPT-4o Mini
* Interactive Streamlit web interface

---

## 🛠️ Tech Stack

* Python
* Streamlit
* LangChain
* FAISS
* OpenAI API
* PyPDFLoader
* python-dotenv

---

## 📂 Project Structure

```
project/
│
├── app.py
├── .env
├── requirements.txt
├── README.md
└── sample.pdf
```

---

## 📦 Installation

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/pdf-rag-app.git

cd pdf-rag-app
```

### 2. Create a virtual environment

**Windows**

```bash
python -m venv venv

venv\Scripts\activate
```

**Linux / macOS**

```bash
python3 -m venv venv

source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Environment Variables

Create a `.env` file in the project root.

```env
OPENAI_API_KEY=your_openai_api_key
```

---

## ▶️ Run the Application

```bash
streamlit run app.py
```

The application will open in your browser.

---

## 📖 How It Works

1. Upload a PDF file.
2. The PDF is loaded using `PyPDFLoader`.
3. The text is split into chunks using `RecursiveCharacterTextSplitter`.
4. OpenAI generates embeddings for each chunk.
5. FAISS stores the embeddings for semantic search.
6. When a question is asked:

   * Relevant chunks are retrieved from FAISS.
   * Retrieved context is added to a prompt.
   * GPT-4o Mini generates an answer using only the retrieved context.

---

## 🔄 Workflow

```
PDF
 │
 ▼
Load PDF
 │
 ▼
Split into Chunks
 │
 ▼
Create Embeddings
 │
 ▼
Store in FAISS
 │
 ▼
User Question
 │
 ▼
Retrieve Relevant Chunks
 │
 ▼
GPT-4o Mini
 │
 ▼
Final Answer
```

---

## 📚 Dependencies

```
streamlit
python-dotenv
langchain
langchain-community
langchain-openai
langchain-text-splitters
faiss-cpu
pypdf
openai
```

Install them with:

```bash
pip install streamlit python-dotenv langchain langchain-community langchain-openai langchain-text-splitters faiss-cpu pypdf openai
```

---

## 💡 Example Usage

1. Launch the app.
2. Upload a PDF (research paper, notes, report, etc.).
3. Ask questions such as:

```
What is the main topic?

Summarize the document.

Who are the authors?

What conclusions were drawn?
```

---

## 📸 Application Interface

* Upload PDF
* Process document
* Enter a question
* Receive AI-generated answers based on the document

---

## 🔒 Notes

* Requires a valid OpenAI API key.
* Answers are generated only from the retrieved document context.
* Large PDFs may take longer to process.

---

## 🚀 Future Improvements

* Multiple PDF support
* Chat history
* Source citations
* Streaming responses
* Persistent vector database
* Hybrid search (BM25 + Vector Search)
* Conversation memory
* PDF highlighting
* Drag-and-drop interface

---

