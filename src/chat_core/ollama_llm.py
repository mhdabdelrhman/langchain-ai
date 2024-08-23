from langchain_core.language_models import BaseChatModel, BaseLLM
from langchain_core.embeddings import Embeddings
from langchain_ollama import ChatOllama, OllamaLLM, OllamaEmbeddings


def load_ollama_chat_llm(model_name: str, temperature: float = 0.8) -> BaseChatModel:
    chat_llm = ChatOllama(
        model=model_name,
        temperature=temperature,
    )

    return chat_llm


def load_ollama_llm(model_name: str, temperature: float = 0.8) -> BaseLLM:
    llm = OllamaLLM(
        model=model_name,
        temperature=temperature,
    )

    return llm


def create_ollama_embeddings(model_name: str) -> Embeddings:
    embeddings = OllamaEmbeddings(model=model_name)
    return embeddings
