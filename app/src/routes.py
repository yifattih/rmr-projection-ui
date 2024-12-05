import os
import json
import requests
from flask import Flask, Response, render_template, request, jsonify

app = Flask(__name__)

# Get API url from environent variable
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
    form_data = {"sex": request.form.get('sex'),
                 "units": request.form.get('units'),
                 "age": request.form.get('age'),
                 "weight": request.form.get('weight'),
                 "height": request.form.get('height'),
                 "weight_loss_rate": request.form.get('weight_loss_rate'),
                 "duration": request.form.get('duration')}
    try:
        response = requests.post(api_url, json=form_data)  # type: ignore
        # Decoding response: bytes object -> str object
        #                    8-bit code units object -> string object
        response_bytes = response.content
        response_str = response_bytes.decode("utf-8")
        response = json.loads(response_str)
    except Exception:
        response = {"message": "An error occured!"}
    return jsonify(response)  # type: ignore
