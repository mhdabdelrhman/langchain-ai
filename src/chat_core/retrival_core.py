from typing import Any
from langchain_core.vectorstores import VectorStore
from langchain_core.language_models import BaseChatModel
from langchain.chains import ConversationalRetrievalChain


def create_chat_retrival(
    store: VectorStore, llm: BaseChatModel, chain_type: str, **ret_kwargs: Any
):
    # define retriever
    retriever = store.as_retriever(**ret_kwargs)

    # define chain
    chain = ConversationalRetrievalChain.from_llm(
        llm=llm,
        retriever=retriever,
        chain_type=chain_type,
        return_source_documents=True,
        return_generated_question=True,
    )

    return chain
