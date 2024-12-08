# app/Dockerfile
FROM python:3.11-slim

# Install updates and create user
RUN apt-get autoremove \
    && groupadd -f -r yifattih \
    && useradd -r -g yifattih -m -d /home/yifattih -s /bin/bash yifattih
# 

# Set the working directory for the app
WORKDIR /app

# Set ownership permissions to working directory
RUN chown -R yifattih:yifattih /app

# Change user
USER yifattih 

# Copy app-specific requirements and install them
COPY requirements.txt /app/

# Update pip and and install requirements
RUN pip install --user --upgrade pip \
    && pip install --user --no-cache-dir -r requirements.txt
# 

# Add the user's local bin directory to PATH
ENV PATH="/home/yifattih/.local/bin:$PATH"

# Copy the app code into the container
COPY src/ /app/src/

# Command to run the app (e.g., a Flask app)
CMD ["gunicorn", "--timeout", "0", "-w", "4", "-b", "0.0.0.0:4000", "src.wsgi:app"]