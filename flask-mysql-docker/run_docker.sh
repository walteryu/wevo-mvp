#!/bin/bash
docker-compose down -v
docker-compose up -d --no-deps --build
docker-compose up
