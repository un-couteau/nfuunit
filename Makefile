init: docker-pull docker-build docker-up node-init backend-init frontend-init
down: backend-clear frontend-clear
restart: down init


docker-up:
	docker-compose up -d

docker-down:
	docker-compose down --remove-orphans

docker-pull:
	docker-compose pull

docker-build:
	docker-compose build
