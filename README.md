# Prueba Técnica GSI- API con FastAPI, MongoDB, Docker y Docker Compose

Consiste en el desarrollo de una API utilizando **FastAPI** como framework backend, **MongoDB** como base de datos NoSQL, **PyMongo** para la conexión y manejo de datos, y **Docker** junto con **Docker Compose** para la contenerización y orquestación de los servicios.

## Tecnologías utilizadas

- **Python 3.10+**
- **FastAPI**
- **MongoDB**
- **PyMongo**
- **Docker**
- **Docker Compose**

1. Clona el repositorio:

git clone https://github.com/JuanpaVJ/prueba-tecnica-gsi.git
cd prueba-tecnica-gsi

2. Contenido de archivo .env para ejecutar con docker:
**MONGO_URL=mongodb://db:27017**
**DATABASE_NAME=task_manager**

3. docker-compose up --build o docker compose up --build (depende del os)

4. Las rutas de postman son las siguientes:

Para crear un listado de tasks esta la api de **create_demo_tasks** que acepta un listado de tasks: http://localhost:8000/tasks/create_demo_tasks

- Ver todas las tasks: http://localhost:8000/tasks **GET**
- Ver task especifica (por id): http://localhost:8000/tasks/{task_id} **GET**
- Crear nueva task: http://localhost:8000/tasks **POST**
    - Requiere de los siguientes campos: title, description, status, priority
- Eliminar una task: http://localhost:8000/tasks/{task_id} **DELETE**
- Editar task: http://localhost:8000/tasks/{task_id} **PUT**. En esta se puede mandar solo 1 campo a elección.