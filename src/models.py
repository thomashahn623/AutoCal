from dataclasses import dataclass
from datetime import datetime
from typing import Optional

@dataclass
class Task:
    id: Optional[int]
    title: str
    due_date: Optional[datetime]
    priority: int = 1
    estimated_minutes: int = 60
    completed: bool = False