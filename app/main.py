from typing import List
from uuid import UUID

from fastapi import FastAPI, HTTPException, Response, status

from .schemas import Task, TaskCreate, TaskUpdate
from .storage import store

app = FastAPI(
    title="Task Manager API",
    version="1.0.0",
    description="Простое CRUD-API для управления задачами",
)


@app.post("/tasks/", response_model=Task, status_code=status.HTTP_201_CREATED)
def create_task(payload: TaskCreate) -> Task:
    """Создать новую задачу."""
    return store.create(payload)


@app.get("/tasks/", response_model=List[Task])
def list_tasks() -> List[Task]:
    """Получить список всех задач."""
    return store.list()


@app.get("/tasks/{task_id}", response_model=Task)
def get_task(task_id: UUID) -> Task:
    """Получить задачу по её UUID."""
    task = store.get(task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return task


@app.put("/tasks/{task_id}", response_model=Task)
def update_task(task_id: UUID, payload: TaskUpdate) -> Task:
    """Обновить данные задачи."""
    task = store.update(task_id, payload)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return task


@app.delete("/tasks/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_task(task_id: UUID) -> Response:
    """Удалить задачу по UUID."""
    ok = store.delete(task_id)
    if not ok:
        raise HTTPException(status_code=404, detail="Task not found")
    return Response(status_code=status.HTTP_204_NO_CONTENT)
