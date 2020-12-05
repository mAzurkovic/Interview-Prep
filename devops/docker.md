# Docker Notes
> This has information about some important Docker concepts

## Common Commands
* `docker ps`: Lists all running containers, add `-a` to see stopped ones too
* `docker container prune`: Removes all stopped containers from `ps` list
* `docker pull <image-repo>`: Pulls that latest version by default of the specified image
* `docker run -it <container> bash`: Enter the container and use bash to exectue things within it
* `docker build -t <image>:<tag> -f PATH/Dockerfile .`: Builds a `Dockerfile` into an image, `-t` sets the tage and `-f` tells the context location if `Dockerfile` not in same directory
* `docker run <image>:<tag>`: Create a container from the image, add `-d` to run in detached mode, `--name` to specify container name, `--rm` to automatically remove from
lisy when complete, `-p XXXX:NNNN` exposes prot `NNNN` in container to port `XXXX` on host
* `docker rmi <image>`: Remove an image

## Questions
* What is Docker? A containerization tool used to run an app and all it's dependencies in an isolated process on any host. It wraps everything an app needs (libraries, bins, files) into one 
container.
* How to build an environment agnostic system with Docker? Use volumes to persist data amongst multiple container instances.
* Difference between `COPY` and `ADD` in `Dockerfile`? Nothing, just use `COPY` as it is the standard.
* What is a Docker image? It is a reference that a container used to build itself from (a blueprint). Running an image creates a container. Can be made up of layers of other images and commands.
* What is a Docker Container? It is a running instance of an image. It has its own way of being referenced.
* What are the states a container can have? `Running`, `Exited`, `Restarting`, `Paused`.
* What are the most common instructions in `Dockerfile`: `FROM`: selects the base image to usem `WORKDIR`: sets the working directory of where the app will run in the container,
`COPY <from> <to>`: copies contents from local path to path in container relative to `WORKDIR`, `RUN`: add it when we add something we want to use later in the container, `CMD`: default values that will run when the container is first executed (if multiple, only last one is executed)
* Are stateful or stateless prefered in Docker? Stateless because the application needs to be replicated and it is easier to run across different environments (i.e Dev, Test, Prod). Can also add variables that get populated when being built, pass a metadata file for example.
* Running `docker kill` vs `docker stop`: Running docker stop gives time for the container to spin down, docker kill immediately halts and terminated the process.
