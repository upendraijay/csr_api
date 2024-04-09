from flask import jsonify, request
from app.models import Task

tasks = [
    Task(id=1, title='Task 1', description='This is task 1', done=False),
    Task(id=2, title='Task 2', description='This is task 2', done=False)
]

def get_tasks():
    return jsonify({'tasks': [task.__dict__ for task in tasks]})

def get_task(task_id):
    task = next((task for task in tasks if task.id == task_id), None)
    if task:
        return jsonify({'task': task.__dict__})
    return jsonify({'message': 'Task not found'}), 404

def create_task():
    if not request.json or not 'title' in request.json:
        return jsonify({'message': 'Title is required'}), 400
    task = Task(
        id=tasks[-1].id + 1,
        title=request.json['title'],
        description=request.json.get('description', ""),
        done=False
    )
    tasks.append(task)
    return jsonify({'task': task.__dict__}), 201

def update_task(task_id):
    task = next((task for task in tasks if task.id == task_id), None)
    if not task:
        return jsonify({'message': 'Task not found'}), 404
    if 'title' in request.json:
        task.title = request.json['title']
    if 'description' in request.json:
        task.description = request.json['description']
    if 'done' in request.json:
        task.done = request.json['done']
    return jsonify({'task': task.__dict__})


def delete_task(task_id):
    task = next((task for task in tasks if task.id == task_id), None)
    if not task:
        return jsonify({'message': 'Task not found'}), 404
    tasks.remove(task)
    return jsonify({'message': 'Task deleted'})
