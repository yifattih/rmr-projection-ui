from typing import TypeAlias
from flask import Flask, Response, render_template, request, jsonify
from app.src.bmr import model

app = Flask(__name__)

JSONType: TypeAlias = dict[str, str | None]
number: TypeAlias = int | float


# To hold the data for the table on buffer
response_data = []


def process_form_data(data: JSONType) -> dict[str, str | number]:
    processed_data = {}
    for key, value in data.items():
        try:
            # Convert input number string
            value = float(value)  # type: ignore
        except Exception:
            pass  # Forget if string value is not number
        processed_data.update({key: value})
    return processed_data


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
    form_data = request.json  # Get data from POST request
    try:
        processed_data = process_form_data(data=form_data)  # type: ignore
        # Calculate output from model
        modeller = model.Builder(data=processed_data)  # type: ignore
        modeller.build()
        modeller.calculate()
        response_data = modeller.jasonable_dict()
        response = {
            "message": "Model Run",
            "status": "Success!",
            "data": response_data,
        }
    except Exception:
        response = {
            "message": "Model Run",
            "status": "Failed!",
            "data": [],
        }
    return jsonify(response)


@app.route("/clear", methods=["POST"])
def clear() -> Response:
    """
    Main function to handle AJAX POST requests to clear form fields and plots.

    :return: Empty data
    :rtype: JSON
    """
    response_data.clear()
    response = {
        "message": "Data Clearing",
        "status": "Success!",
        "data_out": response_data,
    }
    return jsonify(response)
