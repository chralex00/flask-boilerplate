include .env

prepare-windows-venv:
	python3 -m venv .venv
	.venv\Scripts\activate
	pip install Flask

prepare-macos-linux-venv:
	python3 -m venv .venv
	. .venv/bin/activate
	pip install Flask

run:
	python -u ./src/main.py

docker-build:
	docker build -t ${DOCKER_IMAGE_NAME} .

docker-down:
	docker-compose down
	docker rmi ${DOCKER_IMAGE_NAME}

docker-up:
	docker-compose up -d

docker-logs:
	docker-compose logs -f ${DOCKER_CONTAINER_NAME} --tail=50