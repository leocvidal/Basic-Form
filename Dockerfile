FROM alpine:latest

# Install necessary packages
RUN apk add --no-cache python3 py3-pip py3-virtualenv

# Create and activate virtual environment
RUN python3 -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

# Upgrade pip and install dependencies
RUN pip install --upgrade pip

# Copy the application code to the container
COPY . /app
WORKDIR /app

# Install application dependencies
RUN pip install -r requirements.txt

# Set the entry point for the application
CMD ["python", "app.py"]