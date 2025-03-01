import os

# Metrics libraries and modules
from opentelemetry import metrics
from opentelemetry.exporter.otlp.proto.grpc.metric_exporter import \
    OTLPMetricExporter
from opentelemetry.sdk.metrics import MeterProvider
from opentelemetry.sdk.metrics.export import (ConsoleMetricExporter,
                                              PeriodicExportingMetricReader)

# -------------------------
# CONFIGURE EXPORTER METRICS
# -------------------------
try:
    otlp_endpoint = os.getenv("OTLP_ENDPOINT")  # Default Alloy endpoint
    assert otlp_endpoint is not None
    metric_exporter = OTLPMetricExporter(
        endpoint=otlp_endpoint
    )  # For sending traces to an observability backend
except ImportError:
    metric_exporter = ConsoleMetricExporter()

# -------------------------
# METRICS CONFIGURATION
# -------------------------
metric_reader = PeriodicExportingMetricReader(
    metric_exporter, export_interval_millis=15000
)
meter_provider = MeterProvider(metric_readers=[metric_reader])
metrics.set_meter_provider(meter_provider)
meter = metrics.get_meter(__name__)
# Example metric (counter)
# request_counter = meter.create_counter(
#     "http_requests_total",
#     description="Total number of HTTP requests",
# )
