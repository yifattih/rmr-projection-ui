# devcontainer/Dockerfile

FROM mcr.microsoft.com/devcontainers/python:1-3.12-bullseye

# Install development dependencies
# RUN apt-get update && apt-get upgrade -y && apt-get install -y

# # Set the working directory
WORKDIR /workspaces

# Update pip
RUN pip install --upgrade pip

# Install additional Python dependencies if needed
COPY requirements.txt .
RUN pip install -r requirements.txt

# Expose development ports (e.g., 5000 for Flask)
# EXPOSE 5000
