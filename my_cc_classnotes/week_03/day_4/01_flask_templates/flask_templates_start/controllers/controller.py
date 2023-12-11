from flask import render_template, request, redirect
from app import app
from models.todo_list import tasks, add_new_task
from models.task import Task
@app.route('/tasks')
def index():
    return render_template('index.html', title='Home', tasks=tasks)

@app.route('/tasks', methods=['POST'])
def add_task():
    # Store the title value in a variable
    task_title = request.form['title']
    # Store the description value in a variable
    task_description = request.form['description']
    # Create a new Task object
    new_task = Task(task_title, task_description, False)
    # Add the new task to the list
    add_new_task(new_task)
    # render index.html
    # This line will just creat a new task every time the browser is refreshed
    # return render_template('index.html', title='Home', tasks=tasks)
    return redirect('/tasks')

