import os
from datetime import datetime, timezone
import requests
from flask import Flask, render_template, request, jsonify
from otel import logger, meter, setup_telemetry, tracer

service_start_time_utc = datetime.now(timezone.utc)

service = Flask(__name__)

setup_telemetry(service)

api_url = os.getenv("API_URL", "http://api:8000")
logger.info(f"API URL: {api_url}")

rmr_endpoint = f"{api_url}/rmr/"
logger.info(f"RMR endpoint: {rmr_endpoint}")

@service.get("/")
def root() -> str:
    """
    Root endpoint that renders the index.html template.
    """
    with tracer.start_as_current_span("root_span"):
        logger.info("Root endpoint called")

        meter.create_counter(
            name="root_endpoint_calls",
            description="Counts the number of times the root endpoint is called",
            unit="calls",
        ).add(1)

        return render_template("index.html")

@service.post("/submit")
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
        response = requests.post(rmr_endpoint, json=form_data)
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
    with tracer.start_as_current_span("health_span") as span:
        logger.info("Health check endpoint called")

        meter.create_counter(
            name="health_check_requests",
            description="Counts the number of health check requests",
            unit="requests",
        ).add(1)

        current_time_utc = datetime.now(timezone.utc)
        uptime_utc = current_time_utc - service_start_time_utc

        span.set_attribute("health_check.uptime_utc", str(uptime_utc))

        logger.info("Service uptime UTC: %s", uptime_utc)

        health_status = {
            "status": "healthy",
            "uptime_utc": str(uptime_utc),
            "timestamp": str(current_time_utc.isoformat()),
        }

        logger.info("Health check status: %s", health_status)

        meter.create_counter(
            name="health_check_successes",
            description="Counts the number of successful health checks",
            unit="successes",
        ).add(1)

        # Measure service uptime
        meter.create_histogram(
            name="service_uptime",
            description="Measures the service uptime in seconds",
            unit="seconds",
        ).record(uptime_utc.total_seconds())

        return health_status, 200
