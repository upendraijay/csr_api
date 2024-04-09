from app import app

from app.controllers import task_controller,parser_controller



@app.route('/')
def index():
    return 'Hello, World Upendra!'

    
app.route('/compare', methods=['POST'])(parser_controller.compare)
app.route('/label', methods=['POST'])(parser_controller.extract_save)





app.route('/tasks', methods=['GET'])(task_controller.get_tasks)

app.route('/tasks/<int:task_id>', methods=['GET'])(task_controller.get_task)

app.route('/tasks', methods=['POST'])(task_controller.create_task)

app.route('/tasks/<int:task_id>', methods=['PUT'])(task_controller.update_task)

app.route('/tasks/<int:task_id>', methods=['DELETE'])(task_controller.delete_task)
