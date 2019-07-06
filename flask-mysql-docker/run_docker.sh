#!/bin/bash
docker-compose down -v
docker-compose up -d --no-deps --build
docker-compose up

# Restart machine if it cannot connect during package installation:
# docker-machine restart
