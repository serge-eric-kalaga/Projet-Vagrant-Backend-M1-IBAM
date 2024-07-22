from pydantic import BaseModel
from typing import Optional
from api.database import Task
from datetime import datetime


class TaskSchema(BaseModel):
    id: Optional[int] = None
    name: str
    description: Optional[str] = None
    is_completed: Optional[bool] = False
    date_creation: Optional[datetime | str] = None
    date_modification: Optional[datetime | str] = None

class TaskCreateSchema(BaseModel):
    name: str
    description: Optional[str] = None
    is_completed: Optional[bool] = False

class TaskUpdateSchema(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    is_completed: Optional[bool] = False
