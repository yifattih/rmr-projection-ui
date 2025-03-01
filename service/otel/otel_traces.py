import os

# Traces libraries and modules
from opentelemetry import trace
from opentelemetry.exporter.otlp.proto.grpc.trace_exporter import \
    OTLPSpanExporter
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import (BatchSpanProcessor,
                                            ConsoleSpanExporter)

# -------------------------
# CONFIGURE EXPORTER for TRACES
# -------------------------
try:
    otlp_endpoint = os.getenv("OTLP_ENDPOINT")  # Default Alloy endpoint
    assert otlp_endpoint is not None
    trace_exporter = OTLPSpanExporter(
        endpoint=otlp_endpoint
    )  # For sending traces to an observability backend
except ImportError:
    trace_exporter = ConsoleSpanExporter()  # For local debugging

# -------------------------
# TRACE CONFIGURATION
# -------------------------
# Set up the tracer
tracer_provider = TracerProvider()
trace.set_tracer_provider(tracer_provider)
tracer = trace.get_tracer(__name__)
span_processor = BatchSpanProcessor(trace_exporter)
tracer_provider.add_span_processor(span_processor)
