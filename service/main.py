import os
from datetime import datetime, timezone
import requests
from flask import Flask, render_template, request, jsonify
from otel import logger, meter, setup_telemetry, tracer
from models.schemas import InputData, OutputData
from pydantic import ValidationError
import json

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
    with tracer.start_as_current_span("submit_span") as span:
        logger.info("Submit endpoint called")
        
        form_data = request.form.to_dict()
        
        logger.info(f"Received input data: {form_data}")
        
        span.set_attribute("submit.data", json.dumps(form_data))
        
        logger.info("Validating input data")
        try:
            InputData.model_validate(form_data)
            logger.info(f"Input data validated")
        except ValidationError as e:
            logger.error(f"Invalid input data: {e}")
            return jsonify({"message": "Invalid input data", "error": e}), 400

        logger.info("API call")
        try:
            response = requests.post(rmr_endpoint, json=form_data)
            response.raise_for_status()
            response_data = response.json()
            logger.info(f"Sucessful API call")
            span.set_attribute("response.data", json.dumps(response_data))
        except requests.exceptions.ConnectionError as e:
            logger.error("Failed to contact API")
            return jsonify({"error": f"Failed to contact API: {str(e)}"}), 500

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
