# # Step 1: Use an official Python runtime as the base image
# FROM python:3.9-slim

# # Step 2: Set the working directory inside the container
# WORKDIR /app

# # Step 3: Copy the requirements file into the container
# COPY requirements.txt .

# # Step 4: Install the dependencies
# RUN pip install --no-cache-dir -r requirements.txt

# # Step 5: Copy the rest of the application code into the container
# COPY . .

# # Step 6: Expose the port that Flask runs on
# EXPOSE 5000

# # Step 7: Set the environment variable for Flask
# ENV FLASK_APP=app.py
# ENV FLASK_RUN_HOST=0.0.0.0

# # Step 8: Run the Flask application
# CMD ["flask", "run"]

# Use the official Python slim image as a base
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install the Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code into the container
COPY . .

# Expose the port that FastAPI will run on
EXPOSE 8000

# Command to run the FastAPI application using Uvicorn
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
