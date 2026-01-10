from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

users = {}


@app.route('/joke', methods=['GET'])
def return_joke():
    response = requests.get("https://v2.jokeapi.dev/joke/Any")
    joke_data = response.json()

    if joke_data["type"] == "single":
        return joke_data["joke"]
    else:
        return joke_data["setup"] + "\n" + joke_data["delivery"]


@app.route('/joke/<category>', methods=['GET'])
def return_joke_by_category(category):
    response = requests.get(f"https://v2.jokeapi.dev/joke/{category}")
    joke_data = response.json()

    if joke_data["type"] == "single":
        return joke_data["joke"]
    else:
        return joke_data["setup"] + "\n" + joke_data["delivery"]


@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()

    if not data:
        return jsonify({"error": "No data provided"}), 400

    user_name = data.get('user')
    password = data.get('password')

    if not user_name or not password:
        return jsonify({"error": "username and password are required"}), 400

    users[user_name] = password
    return jsonify({user_name: "logged in!"}), 200


if __name__ == '__main__':
    app.run()
