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

```

git clone https://github.com/tu_usuario/tu_repositorio.git
cd tu_repositorio

```


### 2. Crear y activar un entorno virtual
Es recomendable crear un entorno virtual para aislar las dependencias del proyecto:


```
python -m venv venv
```

Luego, activa el entorno virtual:

```
source venv/bin/activate
```


### 3. Instalar las dependencias
Instala las dependencias del proyecto desde el archivo requirements.txt:

```
pip install -r requirements.txt
```

### 4. Configurar Redis (opcional)

Si deseas utilizar Redis para almacenar los resultados en caché, asegúrate de tener Redis instalado y en ejecución en tu máquina local. Si no lo tienes, puedes instalarlo siguiendo la documentación oficial de Redis.

Una vez instalado Redis, puedes iniciar el servicio con el siguiente comando:

En Windows (si tienes Redis instalado como servicio):

```
redis-server
```


## Ejecución del Proyecto

### 1. Ejecutar la API
Una vez que las dependencias estén instaladas y Redis (si lo usas) esté en funcionamiento, puedes iniciar la API utilizando Uvicorn:

```
uvicorn app.main:app --reload
```

Esto iniciará el servidor en http://127.0.0.1:8000. Puedes acceder a la documentación interactiva de la API visitando http://127.0.0.1:8000/docs en tu navegador.

### 2. Ejecutar las Pruebas
Para ejecutar las pruebas, usa pytest. Asegúrate de tener todas las dependencias instaladas y las pruebas se encontrarán en la carpeta test.

```
pytest
```


## Despliegue en Heroku
Para desplegar este proyecto en Heroku, sigue los siguientes pasos:

Instalar la CLI de Heroku si no la tienes instalada. Puedes descargarla desde aquí.

Iniciar sesión en Heroku:

```
heroku login
```

Crear una nueva aplicación en Heroku:

```
heroku create nombre-de-tu-aplicacion
```

Subir el código a Heroku:

```
git push heroku master
```


Abrir la aplicación en tu navegador:

```
heroku open
```

