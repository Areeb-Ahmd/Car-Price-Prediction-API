import json
import redis 
from app.core.config import settings

# Setup redis client
redis_client = redis.Redis.from_url(settings.REDIS_URL)

# Function to return prediction from cache memory
def get_cached_prediction(key: str):
    value = redis_client.get(key)
    if value:
        return json.loads(value)
    return None

#Set the value in cache
def set_cached_prediction(key: str, value: dict, expiry: int = 3600):
    redis_client.setex(key, expiry, json.dumps(value))
