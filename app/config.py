import os
from dotenv import load_dotenv

# Load .env file
load_dotenv()

class Settings:
    PROJECT_NAME: str = "Generative AI Virtual Assistant"
    OPENAI_API_KEY: str = os.getenv("OPENAI_API_KEY")
    PINECONE_API_KEY: str = os.getenv("PINECONE_API_KEY")
    PINECONE_ENV: str = os.getenv("PINECONE_ENV")
    REDIS_HOST: str = os.getenv("REDIS_HOST", "redis")
    REDIS_PORT: int = int(os.getenv("REDIS_PORT", 6379))

settings = Settings()
