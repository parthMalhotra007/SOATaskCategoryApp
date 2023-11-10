from flask import Flask, jsonify, request, abort

app = Flask(__name__)

categories = []

@app.route('/categories', methods=['POST'])
def create_category():
    data = request.get_json()
    category = {
        'id': len(categories) + 1,
        'name': data['name'],
        'description': data['description']
    }
    categories.append(category)
    return jsonify(category), 201

@app.route('/categories', methods=['GET'])
def get_all_categories():
    return jsonify(categories)

@app.route('/categories/<int:category_id>', methods=['GET'])
def get_category(category_id):
    category = next((c for c in categories if c['id'] == category_id), None)
    if category is None:
        abort(404)  # Category not found, return a 404 response
    return jsonify(category)

@app.route('/categories/<int:category_id>', methods=['PUT'])
def update_category(category_id):
    category = next((c for c in categories if c['id'] == category_id), None)
    if category is None:
        abort(404)  # Category not found, return a 404 response

    data = request.get_json()
    category['name'] = data['name']
    category['description'] = data['description']

    return jsonify(category)

@app.route('/categories/<int:category_id>', methods=['DELETE'])
def delete_category(category_id):
    global categories
    categories = [c for c in categories if c['id'] != category_id]
    return '', 204  # No content, successful deletion

if __name__ == '__main__':
    app.run(debug=True, port=5002)
