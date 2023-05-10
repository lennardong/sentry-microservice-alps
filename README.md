[![Deploy to GCP](https://github.com/lennardong/sentry-microservice-alps/actions/workflows/deploy_gcp.yml/badge.svg)](https://github.com/lennardong/sentry-microservice-alps/actions/workflows/deploy_gcp.yml)
[![Dev-CodeCheck](https://github.com/lennardong/sentry-microservice-alps/actions/workflows/dev-codecheck.yml/badge.svg?branch=dev)](https://github.com/lennardong/sentry-microservice-alps/actions/workflows/dev-codecheck.yml)
# sentry-microservice-alps

Automated license plate detection and logging on GCP using a containerized Flask microservice and serverless storage trigger.

## Architecture

- Storage: GCP Cloud Storage
  - simple storage dump for one-shot images of a vehicle
  - filename hardcodes date-time for time of image taken
  - ideally dumped as still-image from a CCTV feed (that will be a seperate implmentation)
- Event Bridge: GCP Functions
  - tiggers on new vehicle image added to storage and runs RESTful request to compute
- Compute: GCP Cloud Run
  - python flask microservice that calls GCP Vision AI
  - uses tag-based identificiation for vehicle -> license plate.
  - does remapping to ortogonal axis to Singapore-based proporotions of license plate and runs OCR for license plate extraction
- Build server: GCP Build

## Repo Structure

pending
