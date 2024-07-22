from fastapi import APIRouter, Depends, HTTPException, status
from api.schemas.tasks import TaskCreateSchema, TaskUpdateSchema, TaskSchema
from api.database import get_db, Session
from api.database.models import Task

router = APIRouter()

@router.get("/tasks", response_model=list[TaskSchema])
async def get_tasks(db:Session=Depends(get_db)):
    tasks = Task.getAll(db)
    return tasks

@router.post("/tasks", response_model=TaskSchema)
async def create_task(task:TaskCreateSchema, db:Session=Depends(get_db)):
    task = Task(
        **task.__dict__
    ).saveWithCommit(db)
    return task.__dict__

@router.get("/tasks/{id}", response_model=TaskSchema)
async def get_task(id:int, db:Session=Depends(get_db)):
    task = Task.get(db, id=id)
    return task
    
@router.put("/tasks/{id}", response_model=TaskSchema)
async def update_task(id:int, data:TaskUpdateSchema, db:Session=Depends(get_db)):
    task = Task.get(db, id=id)

    for key, value in data:
        setattr(task, key, value)

    task.saveWithCommit(db)

    return task