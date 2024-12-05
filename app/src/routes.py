import os
import requests
from typing import TypeAlias
from flask import Flask, Response, render_template, request, jsonify

app = Flask(__name__)

JSONType: TypeAlias = dict[str, str | None]
number: TypeAlias = int | float


# To hold the data for the table on buffer
response_data = []
api_url = os.environ.get("API_URL")


@app.route("/")
def home() -> str:
    """
    Route to handle and render the homepage
    """
    return render_template("index.html")


@app.route("/submit", methods=["POST"])
def submit() -> Response:
    """
    Route to handle form data

    :return: Input and output data
    :rtype: JSON
    """
    # form_data = request.form  # Get data from POST request
    form_data = {"sex": request.form.get('sex'),
                 "units": request.form.get('units'),
                 "age": request.form.get('age'),
                 "weight": request.form.get('weight'),
                 "height": request.form.get('height'),
                 "weight_loss_rate": request.form.get('weight_loss_rate'),
                 "duration": request.form.get('duration')}
    try:
        response = requests.post(api_url, json=form_data) # type: ignore
    except Exception:
        response = {
            "message": "Model Run",
            "status": "Failed!",
            "data": [],
        }
    return jsonify(response.content)
