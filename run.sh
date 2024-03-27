#!/bin/bash

# Build the Docker image
docker build -t to-dox .

# Run the Docker container
docker run -d -p 12345:12345 --name  test to-dox