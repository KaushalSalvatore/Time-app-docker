## Timer-app-docker

### Create a simple flask timer application that containerize an application in Docker and upload in Docker-hub

#### What is docker

```bash
Docker is an open-source platform that enables developers to automate the deployment, scaling, and management of applications inside lightweight, portable containers. Containers package an application along with its dependencies and configurations, ensuring consistency across different environments (development, testing, production).
```

#### Docker Architecture & Components

```bash
Docker follows a client-server architecture and consists of the following key components:

1. Docker Daemon (dockerd):

-> Runs in the background and manages Docker objects (containers, images, networks, volumes).

-> Listens for Docker API requests and executes them.

2. Docker Client (docker CLI)

-> The primary interface for users to interact with Docker.

-> Sends commands to the Docker daemon (e.g., docker run, docker build).

3. Docker Images

-> Read-only templates used to create containers.

-> Built from a Dockerfile (a script containing instructions).

4. Docker Containers

-> Runnable instances of Docker images.

-> Isolated environments where applications execute.

5. Docker Registry (e.g., Docker Hub)

-> A repository for storing and distributing Docker images.

-> Public (Docker Hub) or private registries (AWS ECR, Azure Container Registry).

6. Dockerfile

-> A text file containing instructions to build a Docker image.

-> Defines the base image, dependencies, and application setup.

7. Docker Compose (docker-compose)

-> A tool for defining and running multi-container applications.

-> Uses a YAML file (docker-compose.yml) to configure services.

8. Docker Network

-> Enables communication between containers and external systems.

-> Supports different network drivers (bridge, host, overlay).

9. Docker Volume

-> Persistent storage for containers (data remains after container deletion).

-> Used for databases, logs, and shared data.
```

#### Docker Image

```bash
-> A read-only template containing application code, dependencies, and configurations.

-> Built using a Dockerfile.

-> Stored in layers (each instruction in a Dockerfile creates a new layer).

-> Can be pulled from/pushed to a registry (e.g., docker pull nginx).
```

#### Dockerfile

```bash
-> A script with instructions to build a Docker image.

-> Contains commands like FROM, RUN, COPY, CMD, etc.
```

#### Docker Container

```bash
-> A running instance of a Docker image.

-> Lightweight, isolated, and portable.

-> Can be started, stopped, deleted, or moved between hosts.
```

```bash
Docker simplifies application deployment using containers.

Images are blueprints, containers are running instances.

Dockerfile defines how an image is built.

Docker Hub/Registry stores and distributes images.
```

#### Docker basics Commands

```bash
1. docker image ls  # Images list

2. docker ps       # List running containers

3. docker ps -a    # List container run or stopped both

4. docker ps -a -q  # List id's of container

5. docker stop my-container id/name  # Stop a container

6. docker rm my-container id/name    # Remove a container

7. docker rm $(docker ps -a -q)  # remove all container
             or
   docker container prune  # more reliably

8. docker rmi my-image id/name  # remove images
             or 
   docker image prune -a # remove all the images 

9. docker rmi -f my-image id/name   # remove forcefully

10. docker run my-image id/name  # run docker image

11. docker stop my-container id/name  # stop docker container

12. docker build -t image-name:latest . # create a new image 

13. docker run  -p 5000:5000 --name container-name image-name:latest  # run container with assign ports
Ex. docker run  -p 5000:5000 --name my-timer timer-app:latest

14. docker run -d -p 5000:5000 --name container-name image-name:latest  # run container with detech mode

15. docker system prune -a --volumes  # Remove Everything (Containers + Networks + Images + Volumes)
```

#### Dockerfile 

```bash
FROM python:3-alpine

# Set working directory
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application files
COPY . .

# Expose the port Flask runs on
EXPOSE 5000

# Environment variables
ENV FLASK_APP=app.py
ENV FLASK_ENV=production

# Command to run the application
CMD ["flask", "run", "--host=0.0.0.0"]


FROM: Base image

COPY: Add files to container

RUN: Execute commands during build

CMD: Default command when container starts
```

#### Push to Docker Hub

```bash
docker login

docker tag timer-app kaushalpandey/timer-app:latest

docker push kaushalpandey/timer-app:latest
```