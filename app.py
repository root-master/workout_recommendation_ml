from flask import Flask, jsonify
from flask import request
from flask_cors import CORS
from model import recommend_workout

app = Flask(__name__)
CORS(app)


@app.route("/")
def index():
    return "Flask app is working!"


@app.route("/recommend_workout", methods=["POST", "GET"], strict_slashes=False)
def recommend():
    if request.method == "POST":
        try:
            print(request)
            request_data = request.get_json()
            print(request_data)
            response = recommend_workout(request_data)
            return jsonify(response)
        except Exception as e:
            return "ERROR: " + str(e)

    if request.method == "GET":
        return "THIS IS A MESSAGE FROM /recommend_workout GET"
