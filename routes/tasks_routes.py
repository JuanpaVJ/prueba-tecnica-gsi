from fastapi import APIRouter, HTTPException
from db.connection import db
from models.tasks_model import Task
from services.tasks_services import get_all_tasks, new_task, get_task_by_id, delete_task, update_task, create_demo_tasks
from typing import List

router = APIRouter(prefix="/tasks", tags=["Tasks"])

@router.post("/create_demo_tasks")
async def bulk_insert(tasks: List[Task]):
    return await create_demo_tasks(tasks)

@router.get("/")
async def get_tasks():
    tasks = await get_all_tasks()
    return tasks

@router.post("/")
async def create_task(task: Task):
    task = await new_task(task) 
    return task

@router.get("/{task_id}")
async def get_task(task_id: str):
    task = await get_task_by_id(task_id)
    if task:
        return task
    raise HTTPException(status_code = 404, detail = "Task not found")

@router.delete("/{task_id}")
async def remove_task(task_id: str):
    deleted = await delete_task(task_id)
    if deleted:
        return {"detail": "Task deleted"}
    raise HTTPException(status_code = 404, detail="Task not found")

@router.put("/{task_id}")
async def edit_task(task_id: str, task: Task):
    allowed_status = ['pending', 'in_progress', 'completed']
    
    if 'status' in task.dict(exclude_unset=True):
        status_value = task.status.strip().lower() 
        if status_value not in allowed_status:
            raise HTTPException(status_code=400, detail="Invalid status value. Allowed values are: 'pending', 'in_progress', 'completed'")

    updated = await update_task(task_id, task.dict(exclude_unset=True))
    
    if updated:
        return {"detail": "Task updated"}
    
    raise HTTPException(status_code=404, detail="Task not found or no changes were made.")