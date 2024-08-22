import os
from typing import Any
import chat_core.qdrant_stores as qd
import chat_core.ollama_llm as ol
import chat_core.retrival_core as rt
import chat_core.data_loaders as dl

###################################################

# Langsmith environment variables
if os.getenv("LANGCHAIN_API_KEY") is None:
    os.environ["LANGCHAIN_TRACING_V2"] = "true"
    os.environ["LANGCHAIN_ENDPOINT"] = "https://api.smith.langchain.com"
    os.environ["LANGCHAIN_API_KEY"] = (
        "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"
    )
    os.environ["LANGCHAIN_PROJECT"] = "chat_langchain"

# Qdrant variables
qdrant_connection_string = os.getenv("QDRANT_URL") or "http://localhost:6333"

qdrant_collection_name = os.getenv("QDRANT_COLLECTION_NAME") or "langchain_collection"

# Ollama variables
ollama_model = os.getenv("OLLAMA_MODEL") or "llama3-groq-tool-use"

####################################################


class Chat:
    def __init__(self):
        """
        Initialize the Chat class.
        """
        # Initialize the vector store
        self.store = qd.load_qdrant_store(
            qdrant_connection_string,
            qdrant_collection_name,
            ol.create_ollama_embeddings(ollama_model),
        )

        # Initialize the LLM
        self.chat_llm = ol.load_ollama_chat_llm(ollama_model)

        # Initialize the retriever chain
        self.chain = rt.create_chat_retrival(
            self.store,
            self.chat_llm,
            chain_type="stuff",
            search_type="mmr",
            search_kwargs={"k": 5},
        )

        # Initialize the chat history
        self.chat_history: Any = []

    def ask(self, query: str) -> dict:
        """
        Ask a question and get the answer.

        Args:
            query (str): The question to ask.

        Returns:
            dict: The answer to the question.
        """
        result = self.chain.invoke(
            {"question": query, "chat_history": self.chat_history}
        )
        answer = result["answer"]
        self.chat_history.extend([(query, answer)])

        return result

    def store_pdf_file(self, file_path: str):
        """
        Store a PDF file in the vector store.

        Args:
            file_path (str): The path to the PDF file.
        """
        dl.store_pdf_file(file_path, self.store)

    def clear_chat_history(self):
        """
        Clear the chat history.
        """
        self.chat_history = []

    def set_chat_history(self, chat_history):
        """
        Set the chat history.

        Args:
            chat_history (list): The chat history to set.
        """
        self.chat_history = chat_history
