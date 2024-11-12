import redis

# Configura Redis (puerto y host según el entorno)
redis_client = redis.StrictRedis(host="localhost", port=6379, db=0, decode_responses=True)
