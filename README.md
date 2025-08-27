# CI/CD Pipeline with GitHub Actions & Docker

## 🚀 Overview
This project demonstrates a simple **CI/CD pipeline** that:
1. Runs tests with GitHub Actions.
2. Builds a Docker image.
3. Pushes it to Docker Hub.
4. Can be run locally with Docker Compose.

## 🛠️ Setup
1. Fork/clone repo to your GitHub.
2. Add **GitHub Secrets**:
   - `DOCKERHUB_USERNAME` → your Docker Hub username
   - `DOCKERHUB_TOKEN` → Docker Hub access token
3. Push to `main` branch.

## ▶️ Run locally
```bash
docker pull <your-username>/ci-cd-demo:latest
DOCKERHUB_USERNAME=<your-username> docker-compose up -d
