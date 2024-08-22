from langchain_core.vectorstores import VectorStore
from langchain_core.embeddings import Embeddings
from qdrant_client import QdrantClient
from langchain_qdrant import QdrantVectorStore
from qdrant_client.models import Distance, VectorParams


def load_qdrant_store(
    qdrant_url: str,
    collection_name: str,
    embedding: Embeddings,
    vector_size: int = 4096,
) -> VectorStore:
    qdrant_client = QdrantClient(
        url=qdrant_url, prefer_grpc=True
    )  # Replace with your Qdrant endpoint

    # Create collection if it doesn't exist
    if not qdrant_client.collection_exists(collection_name):
        qdrant_client.create_collection(
            collection_name,
            vectors_config=VectorParams(size=vector_size, distance=Distance.COSINE),
        )

    vector_store = QdrantVectorStore(
        client=qdrant_client,
        collection_name=collection_name,
        embedding=embedding,
    )

    return vector_store
