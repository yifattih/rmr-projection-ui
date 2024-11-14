from typing import TypeAlias
from flask import Flask, Response, render_template, request, jsonify
from bmr import model

app = Flask(__name__)

JSONType: TypeAlias = dict[str, str | None]
number: TypeAlias = int | float


# To hold the data for the table on buffer
data_input = []
data_output = []


def process_data_in(data: JSONType) -> dict[str, str | number]:
    processed_data_in = {}
    for key, value in data.items():
        try:
            value = float(value)  # type: ignore
        except Exception:
            pass
        processed_data_in.update({key: value})
    return processed_data_in


@app.route("/")
def home() -> str:
    """
    Main function to handle and render the homepage.
    """
    return render_template("index.html")


@app.route("/data-input", methods=["GET"])
def get_data_in() -> Response:
    return jsonify(data_input)


@app.route("/data-output", methods=["GET"])
def get_data_out() -> Response:
    return jsonify(data_output)


@app.route("/model", methods=["POST"])
def model_construct() -> Response:
    """
    Main function to handle AJAX POST requests with input data.

    :return: Data received and data output
    :rtype: JSON
    """
    # Get data from AJAX request
    data_in = request.json
    try:
        data_in = process_data_in(data=data_in)  # type: ignore
    except Exception:
        response = {
            "message": "Data Input Conversion",
            "status": "Failed!",
            "data_out": [],
        }

    try:
        # Calculate output from model
        model_engine = model.Builder(data=data_in)  # type: ignore
        model_engine.build()
        model_engine.calculate()
        data_output = model_engine.jasonable_dict()
        response = {
            "message": "Model Run",
            "status": "Success!",
            "data_out": data_output,
        }
    except Exception:
        response = {
            "message": "Model Run",
            "status": "Failed!",
            "data_out": [],
        }

    return jsonify(response)


@app.route("/reset", methods=["POST"])
def clear() -> Response:
    """
    Main function to handle AJAX POST requests to clear form fields and plots.

    :return: Empty data
    :rtype: JSON
    """
    # Get data from AJAX request
    data_input.clear()
    data_output.clear()
    response = {
        "message": "Data Clearing",
        "status": "Success!",
        "data_out": data_output,
    }
    return jsonify(response)
