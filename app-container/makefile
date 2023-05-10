
$(info Current directory: $(CURDIR))

# Docker image name and tag
DOCKER_IMAGE := sentry-image 
DOCKER_TAG :=latest
PROJECT_ID := sentry-microservice-alps

# GCP Variables
IMAGE_NAME := sentry-image
SERVICE_NAME := sentry-service
REGION := asia-southeast1

################################################################################
# DOCKER
################################################################################

# Build Docker image
docker_build_local:
	docker build -t $(DOCKER_IMAGE):$(DOCKER_TAG) .

# Run Docker container
docker_run_local:
	docker run -p 8080:8080 -e PORT=8080 $(DOCKER_IMAGE):$(DOCKER_TAG)

# Clean up images and containers
docker_clean_local:
	docker image rm $(DOCKER_IMAGE):$(DOCKER_TAG)

# Push Docker image to Google Container Registry
docker_push_gcr:
	docker push gcr.io/$(PROJECT_ID)/$(DOCKER_IMAGE):$(DOCKER_TAG)

################################################################################
# GCP
################################################################################

# Deploy to Cloud Run
# 1) build using cloud build 
# 2) push to container registry 
# 3) deploy to Cloud Run

gcp-deploy:
	gcloud builds submit . \
	--config cloudbuild.yaml \
	--substitutions=_PROJECT_ID=${PROJECT_ID},_IMAGE_NAME=${IMAGE_NAME},_SERVICE_NAME=${SERVICE_NAME},_REGION=${REGION} \
	--project ${PROJECT_ID}


################################################################################
# PYTHON
################################################################################

# Install dependencies
install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

# Lint code
lint:
	python -m pylint --disable=R,C --extension-pkg-allow-list=cv2 *.py

# Format code
format:
	python -m black *.py

# Run tests
test:
	python -m pytest -vv --cov=vision --pyargs -k test_vision

# Run tests
# test:
# 	python -m pytest -vv --pyargs -k test_

################################################################################
# OLD
################################################################################
# 
# docker_build_gcr:
# 	docker build -t gcr.io/$(PROJECT_ID)/$(DOCKER_IMAGE):$(DOCKER_TAG) .

# # Deploy to Cloud Build
# google_cloudbuild: 
# 	gcloud builds submit --config cloudbuild.yaml .

# google_gcr_deploy:
# 	gcloud run deploy $(APP_NAME) \
# 		--image gcr.io/$(PROJECT_ID)/$(DOCKER_IMAGE):$(DOCKER_TAG) \
# 		--platform managed \
# 		--allow-unauthenticated
