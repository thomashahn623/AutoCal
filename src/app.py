from flask import Flask, render_template, request, redirect
from db import init_db, add_task, list_tasks, mark_task_completed, remove_task, update_task_due_date
from models import Task
from datetime import datetime

app = Flask(__name__)
init_db()

@app.route("/", methods=["GET", "POST"])
def index():
    error = None
    if request.method == "POST":
        title = request.form.get("title")
        due_raw = request.form.get("due_date")
        priority_raw = request.form.get("priority")
        est_minutes_raw = request.form.get("estimated_minutes")
        try:
            priority = int(priority_raw)
            est_minutes = int(est_minutes_raw)
            if priority < 1 or priority > 5 or est_minutes < 1:
                raise ValueError
        except:
            error = "Please provide valid values for priority (1-5) and minutes (>0)."
        if not error:
            due_date = datetime.fromisoformat(due_raw) if due_raw else None
            task = Task(
                id=None, 
                title=title, 
                due_date=due_date, 
                priority=priority, 
                estimated_minutes=est_minutes
            )
            add_task(task)
            return redirect("/")
    tasks = list_tasks()
    return render_template("index.html", tasks=tasks, error=error)

@app.route("/complete/<int:task_id>", methods=["POST"])
def complete_task(task_id):
    mark_task_completed(task_id)
    return redirect("/")

@app.route("/delete/<int:task_id>", methods=["POST"])
def delete_task(task_id):
    remove_task(task_id)
    return redirect("/")

@app.route("/update/<int:task_id>", methods=["GET", "POST"])
def update_due_date(task_id):
    error = None
    if request.method == "POST":
        new_due_raw = request.form.get("due_date")
        priority_raw = request.form.get("priority")
        est_minutes_raw = request.form.get("estimated_minutes")
        try:
            new_priority = int(priority_raw)
            new_est_minutes = int(est_minutes_raw)
            if new_priority < 1 or new_priority > 5 or new_est_minutes < 1:
                raise ValueError
        except:
            error = "Please provide valid values for priority (1-5) and minutes (>0)."
        if not error:
            new_due = datetime.fromisoformat(new_due_raw) if new_due_raw else None
            update_task_due_date(task_id, new_due, new_priority, new_est_minutes)
        else:
            tasks = list_tasks()
            return render_template("index.html", tasks=tasks, error=error)
    else:
        return redirect("/")
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)