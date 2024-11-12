# Proyecto de Detección de Mutantes

Este proyecto implementa una API para detectar secuencias de ADN mutantes, utilizando FastAPI y Redis para el almacenamiento en caché de los resultados. La API tiene dos endpoints: uno para verificar si una secuencia es mutante y otro para obtener estadísticas sobre las detecciones.

## Requisitos

Antes de ejecutar el proyecto, asegúrate de tener lo siguiente instalado:

- Python 3.8 o superior
- pip (gestor de paquetes de Python)
- Redis (opcional, si se usa para el almacenamiento en caché)

## Instalación

### 1. Clonar el repositorio

Primero, clona el repositorio en tu máquina local:

```bash
git clone https://github.com/tu_usuario/tu_repositorio.git
cd tu_repositorio
2. Crear y activar un entorno virtual
Es recomendable crear un entorno virtual para aislar las dependencias del proyecto:

bash
Copy code
python -m venv venv
Luego, activa el entorno virtual:

En Windows:

bash
Copy code
venv\Scripts\activate
En Mac/Linux:

bash
Copy code
source venv/bin/activate
3. Instalar las dependencias
Instala las dependencias del proyecto desde el archivo requirements.txt:

bash
Copy code
pip install -r requirements.txt
4. Configurar Redis (opcional)
Si deseas utilizar Redis para almacenar los resultados en caché, asegúrate de tener Redis instalado y en ejecución en tu máquina local. Si no lo tienes, puedes instalarlo siguiendo la documentación oficial de Redis.

Una vez instalado Redis, puedes iniciar el servicio con el siguiente comando:

En Windows (si tienes Redis instalado como servicio):

bash
Copy code
redis-server
En Mac/Linux:

bash
Copy code
redis-server
Si no deseas usar Redis, puedes modificar el código para deshabilitar el almacenamiento en caché.

Ejecución del Proyecto
1. Ejecutar la API
Una vez que las dependencias estén instaladas y Redis (si lo usas) esté en funcionamiento, puedes iniciar la API utilizando Uvicorn:

bash
Copy code
uvicorn app.main:app --reload
Esto iniciará el servidor en http://127.0.0.1:8000. Puedes acceder a la documentación interactiva de la API visitando http://127.0.0.1:8000/docs en tu navegador.

2. Ejecutar las Pruebas
Para ejecutar las pruebas, usa pytest. Asegúrate de tener todas las dependencias instaladas y las pruebas se encontrarán en la carpeta test.

bash
Copy code
pytest
Si necesitas especificar una carpeta o archivo en particular para ejecutar los tests, puedes hacerlo de la siguiente manera:

bash
Copy code
pytest test/test_api.py
3. Usar la API
La API tiene los siguientes endpoints:

Endpoint para detectar si una secuencia es mutante
Método: POST
URL: /mutant/
Cuerpo:
json
Copy code
{
  "dna": [
    "ATGCGA",
    "CAGTGC",
    "TTATGT",
    "AGAAGG",
    "CCCCTA",
    "TCACTG"
  ]
}
Respuesta:
Si es mutante: {"status": "Mutant detected"}
Si no es mutante: {"detail": "Not a mutant"}
Endpoint para obtener estadísticas
Método: GET
URL: /stats
Respuesta:
json
Copy code
{
  "count_mutant_dna": 1,
  "count_human_dna": 2,
  "ratio": 0.5
}
Despliegue en Heroku
Para desplegar este proyecto en Heroku, sigue los siguientes pasos:

Instalar la CLI de Heroku si no la tienes instalada. Puedes descargarla desde aquí.

Iniciar sesión en Heroku:

bash
Copy code
heroku login
Crear una nueva aplicación en Heroku:

bash
Copy code
heroku create nombre-de-tu-aplicacion
Subir el código a Heroku:

bash
Copy code
git push heroku master
Escalar los recursos para que la aplicación se ejecute correctamente en Heroku:

bash
Copy code
heroku ps:scale web=1
Abrir la aplicación en tu navegador:

bash
Copy code
heroku open
Contribuciones
Si deseas contribuir al proyecto, puedes seguir estos pasos:

Realiza un fork de este repositorio.
Crea una nueva rama para tus cambios.
Realiza un commit con tus cambios.
Sube tus cambios y abre un pull request.
Licencia
Este proyecto está bajo la Licencia MIT - consulta el archivo LICENSE para más detalles.

markdown
Copy code

### Explicación de los pasos del archivo `README.md`:
- **Instalación de dependencias**: Explica cómo crear un entorno virtual, instalar dependencias y configurar Redis (si se utiliza).
- **Ejecución del proyecto**: Indica cómo iniciar el servidor de la API con `uvicorn` y cómo ejecutar las pruebas con `pytest`.
- **Despliegue en Heroku**: Describe los pasos para desplegar el proyecto en Heroku.
- **Contribuciones**: Explica cómo los desarrolladores pueden contribuir al proyecto.

Este archivo `README.md` proporciona instrucciones claras y fáciles de seguir para que cualquier persona pueda ejecutar el proyecto localmente y contribuir.