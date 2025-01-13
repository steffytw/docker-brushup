# Docker
- Docker is a set of Platforms as a service (PaaS) products that use Operating system-level virtualization to deliver software in packages called containers. 
- It is a platform for developing, shipping, and running applications inside lightweight containers.
- Containers are isolated from one another and bundle their own software, libraries, and configuration files; they can communicate with each other through well-defined channels. 
- All containers are run by a single operating system kernel and therefore use fewer resources than a virtual machine.
- Also containers package an application with all its dependencies, ensuring it runs consistently across different environments.
- Can run the docker image as a docker container in any machine where docker is installed without depending on the operating system.
- Docker makes use of a client-server architecture. 
- The Docker client talks with the docker daemon which helps in building, running, and distributing the docker containers. 
- The Docker client runs with the daemon on the same system or we can connect the Docker client with the Docker daemon remotely. With the help of REST API over a UNIX socket or a network, the docker client and daemon interact with each other.

## Key Concepts:
- Images: Blueprints for containers; created using a Dockerfile.
- Containers: Running instances of Docker images.
- Dockerfile: A text file with instructions to build a Docker image.
- Docker Hub: A registry for Docker images.
- Volumes: Mechanism to persist data outside containers.
- Networking: Connects containers to each other or the internet.

## Dockerfile
- The Dockerfile uses DSL (Domain Specific Language) and contains instructions for generating a Docker image. Dockerfile will define the processes to quickly produce an image. Docker daemon runs all of the instructions from top to bottom.
- (The Docker daemon, often referred to simply as “Docker,” is a background service that manages Docker containers on a system.)
- It is a text document that contains necessary commands which on execution help assemble a Docker Image.
Docker image is created using a Dockerfile.

##  Docker Image
- It is a file, comprised of multiple layers, used to execute code in a Docker container.
-  They are a set of instructions used to create docker containers.
-  Docker Image is an executable package of software that includes everything needed to run an application
-  This image informs how a container should instantiate, determining which software components will run and how.
-  Docker Container is a virtual environment that bundles application code with all the dependencies required to run the application.
-  The application runs quickly and reliably from one computing environment to another.

## Docker Container
-  Docker container is a runtime instance of an image. 
-  Allows developers to package applications with all parts needed such as libraries and other dependencies.
-  Docker Containers are runtime instances of Docker images.
-  Containers contain the whole kit required for an application, so the application can be run in an isolated way. For eg.- Suppose there is an image of Ubuntu OS with NGINX SERVER when this image is run with the docker run command, then a container will be created and NGINX SERVER will be running on Ubuntu OS.

##  Docker Compose
-  Docker Compose will execute a YAML-based multi-container application.
-  The YAML file consists of all configurations needed to deploy containers Docker Compose , which is integrated with Docker Swarm , and provides directions for building and deploying containers. With Docker Compose, each container is constructed to run on a single host.

## Basic commands

```
docker --version              # Check Docker version
docker run hello-world        # Run your first container
docker images                 # List downloaded images
docker ps                     # List running containers
docker ps -a                  # List all containers (running and stopped)
docker stop <container_id>    # Stop a running container
docker rm <container_id>      # Remove a stopped container
docker rmi <image_id>         # Remove an image

```
