import os
import redis

# Obtiene la URL de Redis desde el entorno, usa la configuración local si no está definida
redis_url = os.getenv("REDIS_URL", "redis://localhost:6379/0")

# Establece la conexión con Redis utilizando la URL obtenida
redis_client = redis.StrictRedis.from_url(redis_url, decode_responses=True)
