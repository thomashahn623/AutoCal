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

def mark_task_completed(task_id):
    with get_connection() as conn:
        conn.execute("UPDATE tasks SET completed = 1 WHERE id = ?", (task_id,))
        conn.commit()

def remove_task(task_id):
    with get_connection() as conn:
        conn.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
        conn.commit()

def update_task_due_date(task_id, new_due, new_priority, new_est_minutes):
    with get_connection() as conn:
        conn.execute("""
            UPDATE tasks
            SET due_date = ?, priority = ?, estimated_minutes = ?
            WHERE id = ?;
        """, (
            new_due.isoformat() if new_due else None,
            new_priority,
            new_est_minutes,
            task_id
        ))
        conn.commit()