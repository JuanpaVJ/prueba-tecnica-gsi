from db.connection import db
from models.tasks_model import Task
from bson import ObjectId

tasks_collection = db.tasks

async def get_all_tasks():
    tasks = list(tasks_collection.find())
    for task in tasks:
        task['_id'] = str(task['_id'])
    return tasks

async def new_task(task: Task):
    task_data = task.dict()
    result = tasks_collection.insert_one(task_data)
    task_data['_id'] = str(result.inserted_id)
    return task_data

async def get_task_by_id(id: str):
    task = tasks_collection.find_one({"_id": ObjectId(id)})
    if task:
        task['_id'] = str(task['_id'])
        return task
    return None

async def delete_task(id: str):
    result = tasks_collection.delete_one({"_id": ObjectId(id)})
    return result.deleted_count > 0

async def update_task(task_id: str, task_data: dict):
    result = tasks_collection.update_one(
        {"_id": ObjectId(task_id)},
        {"$set": task_data}
    )
    return result.modified_count > 0
