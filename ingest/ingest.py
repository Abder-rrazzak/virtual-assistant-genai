import sys
import os
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import Pinecone
import pinecone

pinecone.init(
    api_key=os.getenv("PINECONE_API_KEY"),
    environment=os.getenv("PINECONE_ENV")
)

embeddings = OpenAIEmbeddings()

def ingest_text(docs, index_name="assistant-index"):
    Pinecone.from_texts(docs, embeddings, index_name=index_name)
    print(f"Ingested {len(docs)} docs into {index_name}")

if __name__ == "__main__":
    docs = ["This is a sample document about returns policy.",
            "This text explains product warranty terms."]
    ingest_text(docs)
