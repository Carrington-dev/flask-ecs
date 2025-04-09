from src import app
from flask import jsonify

@app.route("/")
def home():
    """
    Returns a description of the API
    ---
    tags:
      - Basic Views
    responses:
      200:
        description: Returns a description of the API
        schema:
          type: object
          properties:
            message:
              type: string
              example: "An AWS ECS CI/CD App For Pipelines"
    """
    return jsonify({
        "message": "An AWS ECS CI/CD App For Pipelines"
    }), 200