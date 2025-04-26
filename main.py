from fastapi import FastAPI
from routes import tasks_routes

app = FastAPI()

app.include_router(tasks_routes.router)
