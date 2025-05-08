from flask import Flask, jsonify, request
from flask_cors import CORS
import test

app = Flask(__name__)
CORS(app)

@app.route("/", methods=['GET'])
def return_home():
    return jsonify({
        'userId': 123,
        'id'    : 321,
        'title' : "W"
    })


if __name__ == "__main__":
    app.run(debug=False, port=8080)