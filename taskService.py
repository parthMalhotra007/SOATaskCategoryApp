from flask import Flask, jsonify, request, abort

app = Flask(__name__)

tasks = []

@app.route('/tasks', methods=['POST'])
def create_task():
    data = request.get_json()
    task = {
        'id': len(tasks) + 1,
        'title': data['title'],
        'description': data['description'],
        'status': data['status'],
        'dueDate': data['dueDate']
    }
    tasks.append(task)
    return jsonify(task), 201

@app.route('/tasks', methods=['GET'])
def get_all_tasks():
    return jsonify(tasks)

@app.route('/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    task = next((t for t in tasks if t['id'] == task_id), None)
    if task is None:
        abort(404)  # Task not found, return a 404 response
    return jsonify(task)

@app.route('/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    task = next((t for t in tasks if t['id'] == task_id), None)
    if task is None:
        abort(404)  # Task not found, return a 404 response

    data = request.get_json()
    task['title'] = data['title']
    task['description'] = data['description']
    task['status'] = data['status']
    task['dueDate'] = data['dueDate']

    return jsonify(task)

@app.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    global tasks
    tasks = [t for t in tasks if t['id'] != task_id]
    return '', 204  # No content, successful deletion

if __name__ == '__main__':
    app.run(debug=True, port=5001)
