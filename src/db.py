import sqlite3
from datetime import datetime
from models import Task

DB_PATH = "autocal.db"

def get_connection():
    return sqlite3.connect(DB_PATH)

def init_db():
    with get_connection() as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS tasks (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                due_date TEXT,
                priority INTEGER DEFAULT 1,
                estimated_minutes INTEGER DEFAULT 60,
                completed INTEGER DEFAULT 0
            );
        """)
        conn.commit()

def add_task(task: Task):
    with get_connection() as conn:
        conn.execute("""
            INSERT INTO tasks (title, due_date, priority, estimated_minutes, completed)
            VALUES (?, ?, ?, ?, ?);
        """, (
            task.title,
            task.due_date.isoformat() if task.due_date else None,
            task.priority,
            task.estimated_minutes,
            int(task.completed)
        ))
        conn.commit()

def list_tasks():
    with get_connection() as conn:
        rows = conn.execute("SELECT * FROM tasks").fetchall()
        return [Task(
            id=row[0],
            title=row[1],
            due_date=datetime.fromisoformat(row[2]) if row[2] else None,
            priority=row[3],
            estimated_minutes=row[4],
            completed=bool(row[5])
        ) for row in rows]