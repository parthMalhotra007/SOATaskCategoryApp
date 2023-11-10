from flask import Flask, jsonify, request, abort
import requests

app = Flask(__name__)

# Define the URLs of the microservices
TASK_SERVICE_URL = "http://localhost:5001"
CATEGORY_SERVICE_URL = "http://localhost:5002"


# API Gateway Routes
@app.route('/tasks', methods=['POST'])
def create_task():
    data = request.get_json()
    response = requests.post(f"{TASK_SERVICE_URL}/tasks", json=data)
    return jsonify(response.json()), response.status_code


@app.route('/tasks', methods=['GET'])
def get_all_tasks():
    response = requests.get(f"{TASK_SERVICE_URL}/tasks")
    return jsonify(response.json()), response.status_code


@app.route('/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    response = requests.get(f"{TASK_SERVICE_URL}/tasks/{task_id}")
    return jsonify(response.json()), response.status_code


@app.route('/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    data = request.get_json()
    response = requests.put(f"{TASK_SERVICE_URL}/tasks/{task_id}", json=data)
    return jsonify(response.json()), response.status_code


@app.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    response = requests.delete(f"{TASK_SERVICE_URL}/tasks/{task_id}")
    return '', response.status_code


@app.route('/categories', methods=['POST'])
def create_category():
    data = request.get_json()
    response = requests.post(f"{CATEGORY_SERVICE_URL}/categories", json=data)
    return jsonify(response.json()), response.status_code


@app.route('/categories', methods=['GET'])
def get_all_categories():
    response = requests.get(f"{CATEGORY_SERVICE_URL}/categories")
    return jsonify(response.json()), response.status_code


@app.route('/categories/<int:category_id>', methods=['GET'])
def get_category(category_id):
    response = requests.get(f"{CATEGORY_SERVICE_URL}/categories/{category_id}")
    return jsonify(response.json()), response.status_code


@app.route('/categories/<int:category_id>', methods=['PUT'])
def update_category(category_id):
    data = request.get_json()
    response = requests.put(f"{CATEGORY_SERVICE_URL}/categories/{category_id}", json=data)
    return jsonify(response.json()), response.status_code


@app.route('/categories/<int:category_id>', methods=['DELETE'])
def delete_category(category_id):
    response = requests.delete(f"{CATEGORY_SERVICE_URL}/categories/{category_id}")
    return '', response.status_code


if __name__ == '__main__':
    app.run(debug=True, port=5000)
