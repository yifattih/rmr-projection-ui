# Stage 1: Build Dependencies
FROM python:3.13-alpine@sha256:18159b2be11db91f84b8f8f655cd860f805dbd9e49a583ddaac8ab39bf4fe1a7 AS builder

# Install necessary dependencies
RUN apk add --no-cache gcc libffi-dev make musl-dev

# Set the working directory for dependency installation
WORKDIR /src

# Copy requirements file
COPY requirements.txt .

# Install dependencies in a temporary directory
RUN pip install --user --no-cache-dir -r requirements.txt

# Stage 2: Final Runtime Image
FROM python:3.13-alpine@sha256:18159b2be11db91f84b8f8f655cd860f805dbd9e49a583ddaac8ab39bf4fe1a7

# Create a group and user (with error handling if already exists)
RUN addgroup -S yifattih \
    && adduser -S yifattih -G yifattih -h /home/yifattih

# Set the working directory
WORKDIR /src

# Set ownership permissions
RUN chown -R yifattih:yifattih /src

# Copy installed dependencies from builder stage
COPY --from=builder /root/.local /home/yifattih/.local

# Add the user's local bin directory to PATH
ENV PATH="/home/yifattih/.local/bin:$PATH"

# Copy only necessary application files
COPY ./src .

# Clean up pycache and .pyc files to reduce image size
RUN find /home/yifattih/.local -type d -name "__pycache__" -prune -exec rm -r {} + \
 && find /home/yifattih/.local -name "*.pyc" -delete \
 && find /src -type d -name "__pycache__" -prune -exec rm -r {} + \
 && find /src -name "*.pyc" -delete

# Disable __pycache__ creation at runtime
ENV PYTHONDONTWRITEBYTECODE=1

# Expose the application port
EXPOSE 8000

# Change user
USER yifattih

# Start the application
CMD ["honcho", "start", "--no-prefix"]