# Makefile

# Command to bring up the Docker Compose services
up:
	docker compose up -d

# Command to bring down the Docker Compose services
down:
	docker compose down

# Command to rebuild the Docker images
build:
	docker compose build

# Command to rebuild and then bring up the Docker Compose services
rebuild: down build up

# Command to bring down and then up the Docker Compose services
run: down up