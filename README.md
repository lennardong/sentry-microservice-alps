[![Main-Deploy to GCP](https://github.com/lennardong/sentry-microservice-alps/actions/workflows/main-deploy-gcp.yml/badge.svg?branch=main)](https://github.com/lennardong/sentry-microservice-alps/actions/workflows/main-deploy-gcp.yml)
[![Dev-CodeCheck](https://github.com/lennardong/sentry-microservice-alps/actions/workflows/dev-codecheck.yml/badge.svg?branch=dev)](https://github.com/lennardong/sentry-microservice-alps/actions/workflows/dev-codecheck.yml)
# sentry-microservice-alps
![concept_pic](https://github.com/lennardong/sentry-microservice-alps/assets/29778721/98619b38-0806-440f-8d9e-af5c15ec006c)
Automated license plate detection and logging on GCP using a containerized Flask microservice and serverless storage trigger.

## Architecture
![System Architecture](https://github.com/lennardong/sentry-microservice-alps/assets/29778721/bc9f76db-a9ab-4bca-ab97-fc807ec87794)

This architecture is designed for flexibility, scalability, and maintainability, based on three key decisions: containerization, serverless triggers, and CI/CD with Makefile and GitHub Actions.

(1) Containerization for Business Logic to Prevent Vendor Lock-in

Containerizing the business logic ensures easy deployment across various platforms, preventing vendor lock-in. The application, currently deployed on GCP, can be seamlessly deployed to other providers. Local container images during development expedite the development cycle.

(2) Serverless Triggers for Scalability and Cost Efficiency

Serverless functions handle event-driven tasks, like processing new images uploaded to the storage bucket. This approach enables automatic scaling and cost efficiency by decoupling processing logic and simplifying the architecture.

(3) CI/CD with Makefile and GitHub Actions for Efficient Development Processes

The CI/CD pipeline, driven by Makefile and GitHub Actions, automates build, test, and deployment steps for quick and reliable code changes and bug fixes. The Makefile abstracts the complexities of the underlying tools, ensuring a consistent interface for managing the application.

## Repo Structure 
```
├── README.md
├── app-container # For microservice
│   ├── resources
│   │   └── car.jpg
│   ├── makefile
│   ├── cloudbuild.yaml
│   ├── dockerfile
│   ├── pytest.ini
│   ├── requirements.txt
│   ├── app.py
│   ├── test_vision.py
│   └── vision.py
└── trigger-serverless # For serverless trigger 
    └── main.py
```

## FAQ

**How was authentication managed?**
- For GCP, authentication was managed via the container image and Google Cloud SDK.
- Credentials were stored locally as an OS variable or on GitHub Actions as a secret.

**Why not use a PaaS architecture?**
- A PaaS architecture would limit flexibility and customization options.
- The current architecture provides more control over the infrastructure, allowing for easy integration of different services and better adaptability to future requirements.

**Why rely on the Makefile? Why not use the built-in deployment triggers in GCP Cloud Build, etc?**
- The Makefile allows for flexibility in development and debugging, enabling development and debugging on local environments such as VSCode.
- It provides a consistent interface for managing the application, regardless of the underlying tools and technologies, making it more portable.

**How is the microservice implemented?**
- It is a Flask microservice acting as a REST API, returning JSON objects of vehicle numbers and colors.
