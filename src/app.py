from flask import Flask, jsonify, request
app = Flask(__name__)

todos = [
    { 
        "label": "My first task", 
        "done": False 
        },
    { 
        "label": "My second task", 
        "done": False 
        }
]

@app.route('/todos', methods=['GET'])
def hello_world():
    json_text = jsonify(todos)
    return json_text


@app.route('/todos', methods=['POST'])
def add_new_todo():
    todos.append(request.json)
    return jsonify(todos)

# fetch URL 
# method: POST
# sample todo
# catch and error


@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    todos.pop(position)
    return jsonify(todos)

# fetch URL 
# method: DELETE
# specify which number in the list to delete
# catch and error


if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)