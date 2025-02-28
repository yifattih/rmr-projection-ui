import logging
import os

# Logs libraries and modules
from opentelemetry import _logs
from opentelemetry.exporter.otlp.proto.grpc._log_exporter import OTLPLogExporter
from opentelemetry.sdk._logs import LoggerProvider, LoggingHandler
from opentelemetry.sdk._logs.export import BatchLogRecordProcessor, ConsoleLogExporter

# from opentelemetry.instrumentation.logging import LoggingInstrumentor

# -------------------------
# CONFIGURE EXPORTER LOGS
# -------------------------
try:
    otlp_endpoint = os.getenv("OTLP_ENDPOINT")  # Default Alloy endpoint
    assert otlp_endpoint != None
    log_exporter = OTLPLogExporter(endpoint=otlp_endpoint)
except:
    log_exporter = ConsoleLogExporter()

# -------------------------
# LOGGING CONFIGURATION
# -------------------------
logger_provider = LoggerProvider()
_logs.set_logger_provider(logger_provider)
log_processor = BatchLogRecordProcessor(log_exporter)
logger_provider.add_log_record_processor(log_processor)

# Set up standard logging
handler = LoggingHandler(level=logging.INFO)
logging.basicConfig(level=logging.INFO, handlers=[handler])
logger = logging.getLogger(__name__)
