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

## 📷screenshots

<img width="1901" height="875" alt="Screenshot 2025-08-28 202851" src="https://github.com/user-attachments/assets/c2be1f24-ffcd-4bf9-bfda-5d467eeb88e8" />

<img width="1899" height="885" alt="Screenshot 2025-08-28 204103" src="https://github.com/user-attachments/assets/dc885fd1-999b-4c9e-aae2-7527f402b26a" />

<img width="1721" height="897" alt="Screenshot 2025-08-30 204945" src="https://github.com/user-attachments/assets/0bd8ca75-9abd-4806-81f9-2661b0b26c99" />

<img width="1914" height="605" alt="Screenshot 2025-08-30 210302" src="https://github.com/user-attachments/assets/807c6790-807c-44b1-8247-aa4b6204828a" />






