from . import otel_logs, otel_metrics, otel_traces
from opentelemetry.instrumentation.logging import LoggingInstrumentor

meter = otel_metrics.meter
logger = otel_logs.logger
tracer = otel_traces.tracer

try:
    from opentelemetry.instrumentation.fastapi import FastAPIInstrumentor # type: ignore
    instrumentator = FastAPIInstrumentor()
    log_message = "FastAPI instrumentator initialized"
except:
    from opentelemetry.instrumentation.flask import FlaskInstrumentor # type: ignore
    instrumentator = FlaskInstrumentor()
    log_message = "Flask instrumentator initialized"
finally:
    logger.info(log_message)

def setup_telemetry(app) -> None:
    """Sets up OpenTelemetry instrumentation for FastAPI."""

    # Instrument FastAPI
    instrumentator.instrument_app(app)

    # Instrument Python standard logging
    LoggingInstrumentor().instrument(
        set_logging_format=True,
        logging_format="%(asctime)s %(levelname)s %(name)s %(filename)s:%(lineno)d %(otelTraceID)s %(otelSpanID)s %(message)s",
    )

    logger.info("Telemetry configuration done")

    # Example: Increment metric when setting up telemetry
    # request_counter.add(1, {"method": "setup_telemetry"})
