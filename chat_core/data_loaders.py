from langchain_core.vectorstores import VectorStore
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import (
    # CharacterTextSplitter,
    RecursiveCharacterTextSplitter,
)


def store_pdf_file(
    file_path: str, vector_store: VectorStore, chunk_size=1000, chunk_overlap=150
):
    loader = PyPDFLoader(file_path)
    pages = loader.load()
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size, chunk_overlap=chunk_overlap
    )
    print("pages len", len(pages))
    docs = text_splitter.split_documents(pages)
    print("docs len", len(docs))
    vector_store.add_documents(docs)
