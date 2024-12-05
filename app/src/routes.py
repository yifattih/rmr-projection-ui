import os
import requests
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Get API URL from environment variable
api_url = os.environ.get("API_URL")
if not api_url:
    raise EnvironmentError("API_URL environment variable not set.")


@app.route("/")
def home() -> str:
    """
    Render the homepage.

    :return: Rendered homepage HTML.
    :rtype: str
    """
    return render_template("index.html")


@app.route("/submit", methods=["POST"])
def submit():
    """
    Process form data submitted from the frontend and send it to the API.

    :return: API response as JSON.
    :rtype: Response
    """
    form_data = {
        "sex": request.form.get("sex"),
        "units": request.form.get("units"),
        "age": request.form.get("age"),
        "weight": request.form.get("weight"),
        "height": request.form.get("height"),
        "weight_loss_rate": request.form.get("weight_loss_rate"),
        "duration": request.form.get("duration"),
    }

    # Validate input data
    for key, value in form_data.items():
        if not value:
            return jsonify({"error": f"Missing value for {key}"}), 400

    try:
        response = requests.post(api_url, json=form_data)
        response.raise_for_status()
        response_data = response.json()
    except requests.exceptions.RequestException as e:
        return jsonify({"error": f"Failed to contact API: {str(e)}"}), 500
    except ValueError:
        return jsonify({"error": "Invalid JSON response from API"}), 500

    return jsonify(response_data)
