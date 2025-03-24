from flask import Flask, render_template, request, redirect
from db import init_db, add_task, list_tasks
from models import Task
from datetime import datetime

app = Flask(__name__)
init_db()

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        title = request.form.get("title")
        due_raw = request.form.get("due_date")
        due_date = datetime.fromisoformat(due_raw) if due_raw else None
        task = Task(id=None, title=title, due_date=due_date)
        add_task(task)
        return redirect("/")
    
    tasks = list_tasks()
    return render_template("index.html", tasks=tasks)

if __name__ == "__main__":
    app.run(debug=True)