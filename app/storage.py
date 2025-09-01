from threading import Lock
from typing import Dict, List
from uuid import UUID, uuid4

from .schemas import Task, TaskCreate, TaskUpdate

class InMemoryStorage:
    """Простое потокобезопасное хранилище в памяти"""
    def __init__(self) -> None:
        self._data: Dict[UUID, Task] = {}
        self._lock = Lock()

    def create(self, payload: TaskCreate) -> Task:
        task = Task(uuid=uuid4(), **payload.model_dump())
        with self._lock:
            self._data[task.uuid] = task

        return task
    
    def list(self) -> List[Task]:
        return list(self._data.values())

    def get(self, task_id: UUID) -> Task | None:
        return self._data.get(task_id)

    def update(self, task_id: UUID, payload: TaskUpdate) -> Task | None:
        with self._lock:
            current = self._data.get(task_id)
            if not current: 
                return None
            
            data = current.model_dump()
            patch = payload.model_dump(exclude_unset=True)
            data.update(patch)
            updated = Task(**data)
            self._data[task_id] = updated
            return updated

    def delete(self, task_id: UUID) -> bool:
        with self._lock:
            return self._data.pop(task_id, None) is not None

store = InMemoryStorage()

