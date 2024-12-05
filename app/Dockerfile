# app/Dockerfile
FROM python:3.11-slim

# Install updates
RUN apt-get update && apt-get upgrade -y && apt-get install -y

# Set the working directory for the app
WORKDIR /app

# Update pip
RUN pip install --upgrade pip

# Copy app-specific requirements and install them
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copy the app code into the container
COPY src/ /app/src/

# Create port environment variable
ENV API_URL = "https://api-alpha-577926260607.us-central1.run.app/rmr/"

# Expose the application port
EXPOSE 5000

# Command to run the app (e.g., a Flask app)
CMD ["python", "src/wsgi.py"]