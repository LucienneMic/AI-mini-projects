# Build an AI developer assistant

<details open>
 <summary> :books:General Notes - Click Here</summary>

### What is FastAPI?

FastAPI is a popular web framework for building APIs with Python, based on standard Python type hints. It is intuitive and easy to use, and it can provide a production-ready application in a short period of time. It is fully compatible with OpenAPI and JSON Schema.
https://fastapi.tiangolo.com/

### What is Docker?

Docker is a tool that packages an app and everything it needs (like code, libraries, and settings) into a container. This container can run anywhere, making it easier to move the app between computers without worrying about compatibility issues.
https://www.docker.com/

</details>

## Overview

AI Developer Assistant is a microservice-based backend system that provides AI-powered developer assistance via REST APIs.
The project demonstrates modern backend engineering practices including:

- Microservices and service-to-service communication
- Cloud deployment readiness
- CI/CD pipelines and automated testing

Docker was used to containerize and deploy the application for consistent and scalable deployment.

### Docker
1. If docker is not installed - use this link
https://docs.docker.com/desktop/setup/install/mac-install/#install-interactively

2. Open http://localhost:8088/ to make sure that docker was correctly installed

### Architecture

- API Service: exposes REST endpoints for client requests
- AI Service: handles AI prompt generation (mocked or real LLM)
- Communication: service-to-service over HTTP
- Containerization: Docker for isolated environments

### Tech Stack

- Python, FastAPI
- Docker & docker-compose
- GitHub Actions (CI/CD)
- Pytest for automated testing
- Deployed on AWS / GCP

### Features

- REST API for submitting developer prompts
- AI service integration using LLM APIs
- Stateless services for horizontal scalability
- Automated test suite

### Docker Usage

#### Build and Run
```
docker-compose up --build
```

**API Service:** accessible at http://localhost:8000

**AI Service:** accessible at http://localhost:8001 (optional direct access)

##### Example Requests

Health check:
```
curl http://localhost:8000/health
```

Send prompt:
```
curl -X POST "http://localhost:8000/prompt?prompt=Hello"
```

### CI/CD

- GitHub Actions pipeline runs tests and builds Docker images on every push
- Fails builds on test failures

### Tests

Run tests locally with Pytest:
```
pytest services/api/tests
pytest services/ai_service/tests
```

### Deployment

- Containerized services deployed to cloud infrastructure
- Environment variables used for configuration
- Supports local development and cloud deployment




