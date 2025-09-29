import redis
import os

redis_client = redis.Redis(
    host=os.getenv("REDIS_HOST", "localhost"),
    port=int(os.getenv("REDIS_PORT", 6379)),
    decode_responses=True
)

def save_message(session_id, role, content):
    redis_client.rpush(session_id, f"{role}:{content}")

def load_conversation(session_id):
    return redis_client.lrange(session_id, 0, -1)
