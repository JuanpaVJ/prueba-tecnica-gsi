from pydantic import BaseModel
from datetime import datetime, timedelta

default_time = datetime.now() + timedelta(hours=-6)
time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

class Task(BaseModel):
    title: str = "New Task"
    description: str = None
    status: str = "Pending"
    priority: str = "Medium"
    created_at: datetime = time
    updated_at: datetime = time
    due_date: datetime = None