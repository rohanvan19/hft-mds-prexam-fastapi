# hft-mds-prexam-fastapi

This project is a full-stack web application where we have used **FastAPI** as the frontend framework and **Spring Boot** as the backend framework. **The frontend application runs on port 8000.**

## Project Overview

The goal of this project is to demonstrate the integration between **FastAPI** (a modern, fast web framework for building APIs with Python) for the frontend and **Spring Boot** (a framework to create Java-based applications) for the backend. We use Docker for containerization of both the frontend and backend services.

## Tech Stack

- **Frontend**: FastAPI
- **Backend**: Spring Boot (Java)
- **Containerization**: Docker
- **Database**: PostgreSQL (via Docker)

## Features

- FastAPI is used to handle requests, serve the frontend, and manage API calls.
- Spring Boot serves as the backend to handle business logic and manage the database interactions.
- The backend is connected to a PostgreSQL database running in a Docker container.
- Docker images for both frontend and backend are created and pushed to Docker Hub for easy deployment.

## How to Run the Project Locally

### Prerequisites
- Install Docker on your machine.
- Make sure you have access to the internet to pull the Docker images.

### Steps

#### 1. Clone the Repository
```bash
git clone https://github.com/rohanvan19/hft-mds-prexam-fastapi.git
cd hft-mds-prexam-fastapi
