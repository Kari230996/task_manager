from enum import Enum
from typing import Optional
from uuid import UUID

from pydantic import BaseModel, Field

class Status(str, Enum):
    created = "created"
    in_progress = "in_progress"
    done = "done"


class TaskBase(BaseModel):
    title: str = Field(..., min_length=1, max_length=200)
    description: Optional[str] = Field("", max_length=2000)
    status: Status = Status.created

class TaskCreate(TaskBase):
    pass

class TaskUpdate(BaseModel):
    title: Optional[str] = Field(None, min_length=1, max_length=200)
    description: Optional[str] = Field(None, max_length=2000)
    status: Optional[Status] = None


class Task(TaskBase):
    uuid: UUID