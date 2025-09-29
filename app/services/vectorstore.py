import os
import pinecone
from langchain.vectorstores import Pinecone
from langchain.embeddings.openai import OpenAIEmbeddings

# Init Pinecone
pinecone.init(
    api_key=os.getenv("PINECONE_API_KEY"),
    environment=os.getenv("PINECONE_ENV")
)

embeddings = OpenAIEmbeddings()

def get_vectorstore(index_name="assistant-index"):
    return Pinecone.from_existing_index(index_name, embeddings)
