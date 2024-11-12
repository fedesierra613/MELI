import os
import redis
from dotenv import load_dotenv

# Carga variables de entorno desde un archivo .env en modo de desarrollo
load_dotenv()

# Obtiene la URL de Redis desde el entorno, usa la configuración local si no está definida
redis_url = os.getenv("REDIS_URL", "redis://localhost:6379/0")
redis_client = redis.StrictRedis.from_url(redis_url, decode_responses=True)
