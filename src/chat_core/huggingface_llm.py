from langchain_core.language_models import BaseChatModel, BaseLLM
from langchain_core.embeddings import Embeddings
from langchain_huggingface import (
    ChatHuggingFace,
    HuggingFacePipeline,
    HuggingFaceEmbeddings,
)
from transformers import AutoModelForCausalLM, AutoTokenizer, pipeline


def load_hf_chat_llm(
    model_name: str,
    task: str = "text-generation",
) -> BaseChatModel:
    llm = load_hf_llm(model_name=model_name, task=task)
    chat_llm = ChatHuggingFace(llm=llm)

    return chat_llm


def load_hf_llm(
    model_name: str,
    task: str = "text-generation",
) -> BaseLLM:
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForCausalLM.from_pretrained(model_name)

    pipe = pipeline(task, model=model, tokenizer=tokenizer)

    llm = HuggingFacePipeline(pipeline=pipe)

    return llm


def create_hf_embeddings(model_name: str) -> Embeddings:
    return HuggingFaceEmbeddings(model_name=model_name)
