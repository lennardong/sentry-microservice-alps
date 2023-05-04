################################################################################
# DOCKER
################################################################################

# Application name
APP_NAME=sentry

# Docker image name and tag
DOCKER_IMAGE=lennardong/$(APP_NAME)
DOCKER_TAG=latest

# Build Docker image
build:
	docker build -t $(DOCKER_IMAGE):$(DOCKER_TAG) .

# Run Docker container
run:
	docker run -p 8080:8080 -e PORT=8080 $(DOCKER_IMAGE):$(DOCKER_TAG)

# Clean up images and containers
clean:
	docker image rm $(DOCKER_IMAGE):$(DOCKER_TAG)


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
