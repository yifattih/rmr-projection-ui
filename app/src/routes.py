from typing import TypeAlias
from flask import Flask, Response, render_template, request, jsonify
from bmr import model

app = Flask(__name__)

JSONType: TypeAlias = dict[str, str | None]
number: TypeAlias = int | float


# To hold the data for the table on buffer
response_data = []


def process_form_data(data: JSONType) -> dict[str, str | number]:
    processed_data = {"sex": data["sex"],
                      "units": data["units"],
                      "age": float(data["age"]),
                      "weight": float(data["weight"]),
                      "height": float(data["height"]),
                      "rate": float(data["rate"]),
                      "time": int(data["time"])
                      }
    return processed_data


@app.route("/")
def home() -> str:
    """
    Route to handle and render the homepage
    """
    return render_template("index.html")


@app.route("/submit", methods=["POST"])
def submit() -> Response:
    # data = request.form
    # response = {"message": "Data received successfully!",
    #             "data": data}
    # return jsonify(response)
    """
    Route to handle form data

    :return: Input and output data
    :rtype: JSON
    """
    form_data = request.form  # Get data from POST request
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
