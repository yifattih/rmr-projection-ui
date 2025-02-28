import os
from datetime import datetime, timezone
import requests
from flask import Flask, render_template, request, jsonify
from otel import logger, meter, setup_telemetry, tracer

service_start_time_utc = datetime.now(timezone.utc)

service = Flask(__name__)

setup_telemetry(service)

try:
    api_url = os.environ.get("API_URL")
    assert api_url != None
    api_health = {"message": requests.get(f"{api_url}/health").text,
                  "status_code": requests.get(f"{api_url}/health").status_code}
except AssertionError:
    api_health = {"message": "API_URL environment variable not set",
                  "status_code": 500}
except requests.exceptions.MissingSchema as e:
    api_health = {"message": "Wrong URL schema for API_URL",
                  "status_code": 500}

api_endpoint = "/rmr/"


@service.get("/")
def root() -> str:
    """
    Root endpoint that renders the index.html template.
    """
    return render_template("index.html")

@service.route("/submit", methods=["POST"])
def submit():
    """
    Endpoint to process submitted form data, call API for RMR calculations,
    and return results back.
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
        response = requests.post(f"{api_url}{api_endpoint}", json=form_data)
        response.raise_for_status()
        response_data = response.json()
    except requests.exceptions.RequestException as e:
        return jsonify({"error": f"Failed to contact API: {str(e)}"}), 500
    except ValueError:
        return jsonify({"error": "Invalid JSON response from API"}), 500

    return jsonify(response_data)

@service.get('/health')
def health_check():
    """
    Endpoint that returns the status of the service.
    """
    current_time_utc = datetime.now(timezone.utc)
    uptime_utc = current_time_utc - service_start_time_utc

    health_status = {
        "status": "healthy",
        "uptime_utc": str(uptime_utc),
        "timestamp": str(current_time_utc.isoformat()),
    }
    return health_status, 200
