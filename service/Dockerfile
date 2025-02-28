# Stage 1: Build Dependencies
FROM python:3.11-alpine AS builder

# Install necessary dependencies
RUN apk add --no-cache gcc libffi-dev make musl-dev

# Set the working directory for dependency installation
WORKDIR /service

# Copy requirements file
COPY requirements.txt /service/

# Install dependencies in a temporary directory
RUN pip install --user --no-cache-dir -r requirements.txt

# Stage 2: Final Runtime Image
FROM python:3.11-alpine

# Create a group and user (with error handling if already exists)
RUN addgroup -S yifattih \
    && adduser -S yifattih -G yifattih -h /home/yifattih

# Set the working directory
WORKDIR /service

# Set ownership permissions
RUN chown -R yifattih:yifattih /service

# Change user
USER yifattih

# Copy installed dependencies from builder stage
COPY --from=builder /root/.local /home/yifattih/.local

# Add the user's local bin directory to PATH
ENV PATH="/home/yifattih/.local/bin:$PATH"

# Copy only necessary application files
COPY Procfile main.py /service/
COPY models /service/models
COPY otel /service/otel
COPY static /service/static
COPY templates /service/templates


# Expose the application port
EXPOSE 8000

# Start the application
CMD ["honcho", "start", "--no-prefix"]