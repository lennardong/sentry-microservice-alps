################################################################################
# DOCKER
################################################################################

# Application name
APP_NAME=sentry

# Docker image name and tag
DOCKER_IMAGE=$(APP_NAME)
DOCKER_TAG=latest
PROJECT_ID=sentry-microservice-alps

# Build Docker image
docker_build_local:
	docker build -t $(DOCKER_IMAGE):$(DOCKER_TAG) .

docker_build_gcr:
	docker build -t gcr.io/$(PROJECT_ID)/$(DOCKER_IMAGE):$(DOCKER_TAG) .

# Push Docker image to Google Container Registry
docker_push_gcr:
	docker push gcr.io/$(PROJECT_ID)/$(DOCKER_IMAGE):$(DOCKER_TAG)

# Run Docker container
docker_run_local:
	docker run -p 8080:8080 -e PORT=8080 $(DOCKER_IMAGE):$(DOCKER_TAG)

# Clean up images and containers
docker_clean_local:
	docker image rm $(DOCKER_IMAGE):$(DOCKER_TAG)

# Deploy to Cloud Run
google_gcr_deploy:
	gcloud run deploy $(APP_NAME) \
		--image gcr.io/$(PROJECT_ID)/$(DOCKER_IMAGE):$(DOCKER_TAG) \
		--platform managed \
		--allow-unauthenticated


################################################################################
# PYTHON
################################################################################

# Install dependencies
install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

# Lint code
lint:
	pylint --disable=R,C *.py

# Format code
format:
	black *.py

# Run tests
test:
	pytest -vv --cov=$(APP_NAME) tests/
