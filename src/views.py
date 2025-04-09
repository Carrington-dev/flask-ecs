from src import app
from flask import jsonify

@app.route("/")
def home():
    return jsonify({
        "status": "An AWS ECS CI/CD App For Pipelines"
    }), 200