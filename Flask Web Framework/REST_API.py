from flask import Flask, request, jsonify
import json

app = Flask(__name__)
user_name = ""
user1 = {"name": "Alice", "phone": "1234567"}
user2 = {"name": "Bob", "phone": "7654321"}
users = {101: user1, 102: user2}
user_id = 103


@app.route("/")
def hello_world():
    return "Hello, World!\n"


@app.route('/name', methods=['POST'])
def save_name():
    global user_name
    data = request.get_json()
    user_name = data.get('name')
    return json.dumps({"name": user_name})


@app.route('/name', methods=['GET'])
def load_name():
    return user_name


####################################################################################

@app.route('/users', methods=['GET'])
def get_all_users():
    if not users:
        return jsonify([]), 200

    user_list = []
    for k, v in users.items():
        user_dict = {"id": k, "name": v.get("name")}
        user_list.append(user_dict)

    return jsonify(user_list), 200


@app.route('/users/<int:id>', methods=['GET'])
def get_user(id):
    if id in users:
        return jsonify(users[id]), 200
    else:
        return jsonify({"error": f"User ID {id} does not exist."}), 404


@app.route('/users', methods=['POST'])
def create_user():
    global user_id
    data = request.get_json()
    name = data.get('name')
    phone = data.get('phone')
    if not name or not phone:
        return jsonify({"error": "Name and phone are required"}), 400

    user_dict = {"name": name, "phone": phone}
    users[user_id] = user_dict
    current_id = user_id
    user_id += 1
    return jsonify({"id": current_id}), 201


@app.route('/users/<int:id>', methods=['PUT'])
def update_user(id):
    data = request.get_json()
    name = data.get('name')
    phone = data.get('phone')
    if not name or not phone:
        return jsonify({"error": "Name and phone are required"}), 400

    user_dict = {"name": name, "phone": phone}
    if id in users:
        users[id] = user_dict
        return jsonify({id: "updated"}), 200
    else:
        return jsonify({"error": f"No user with id: {id} exists."}), 404


@app.route('/users/<int:id>', methods=['DELETE'])
def delete_user(id):
    if id in users:
        users.pop(id)
        return jsonify({id: "deleted"}), 200
    else:
        return jsonify({"error": f"No user with id: {id} exists."}), 404


if __name__ == '__main__':
    app.run()
