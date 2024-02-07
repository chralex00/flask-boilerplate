# flask-boilerplate
A boilerplate for a Flask project.

This boilerplate contains the minimum needed to start a Flask project. The idea is to provide only and exclusively the basic scaffolding and utilities to develop a service with Flask.

This boilerplate has the fllowing utilities:
- [Flask](https://flask.palletsprojects.com/)
- SQLite3 (part of the Python Standard Library)
- API Docs, made with [Postman](https://www.postman.com/)
- UML Docs, made with [Draw.io](https://app.diagrams.net/)
- [GNU Make](https://www.gnu.org/software/make/)
- [Docker](https://www.docker.com/)

What's in this project? This is a simple project that uses a SQLite3 database to expose a CRUD REST APIs on a very simple entity, Person.

## Prerequisites
The following dependencies are required:
- Python ^3.12.1
- Pip ^23.2.1

The following dependencies are optional, but are still very convenient:
- Docker ^24.0.7
- Docker Compose ^2.23.3
- GNU Make ^3.81

## Configuration
This service can be configured by a .env file. Run the following command:
```bash
cp env_example .env
```
to copy the env_example content into the .env file, then modify the environment variables.

The env_example has the following env vars:
- `LISTENING_PORT`: the listening port of the service. For example, `3001`, or `8081`. It's required.
- `DATABASE_NAME`: the database name (including the `.db` extension), like `flask-boilerplate.db`. It's required
- `DOCKER_CONTAINER_NAME`: the container name, like `flask-boilerplate`. It's useful to run the dockerized service.
- `DOCKER_IMAGE_NAME`: the container name, like `flask-boilerplate`. It's useful to run the dockerized service.
- `DOCKER_PORT`: the listening port of the dockerized service, like `8081`, or `8088`. It's useful to run the dockerized service.

## Preparation
First of all, prepare and activate a Python VENV (Virtual ENVironment):
```bash
# for Windows
python3 -m venv .venv
.venv\Scripts\activate
# or
make prepare-windows-venv

# for MacOS, or Linux
python3 -m venv .venv
. .venv/bin/activate
# or
make prepare-macos-linux-venv
```

## Installation
Once the environment has been prepared, all we have to do is install all dependencies with PIP:
```bash
pip install -r requirements.txt
```

It is not necessary to install any SQLite3 library, since it is already part of the Python Standard Library.

## Running
Run in development mode:
```bash
python -u ./src/main.py
# or
make run
```

## Running the dockerized service
Build the docker image with the following command:
```bash
docker build -t flask-boilerplate .
# or
make docker-build
```

Then, run the dockerized service:
```bash
docker-compose up -d
# or
make docker-up
```
## Stopping the dockerized service
Stop the dockerized service:
```bash
docker-compose down
# or
make docker-down
```

## Inspect the dockerized service
See container logs:
```bash
docker-compose logs -f flask-boilerplate --tail=50
# or
make docker-logs
```

## Contacts
Don't hesitate to contact me for any info, bugs, or improvements! Below are my contacts:
- [GitHub](https://github.com/chralex00)
- [Email](mailto:christian.alessandro.atzeni.00@outlook.com)