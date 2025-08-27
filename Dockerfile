# Use the official Python image
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy requirements and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application
COPY . .

# Configuration for Cloud Run
ENV PORT=8080

# Command to run the application
CMD exec gunicorn --bind :$PORT main:app
