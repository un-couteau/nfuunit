CONTAINER_TOOL := $(if $(filter $(CONTAINER),docker),docker,podman)


start: container-up
down: container-down
restart: down init
init: container-pull container-build container-up


container-up:
	$(CONTAINER_TOOL)-compose up -d

container-down:
	$(CONTAINER_TOOL)-compose down --remove-orphans

container-pull:
	$(CONTAINER_TOOL)-compose pull

container-build:
	$(CONTAINER_TOOL)-compose build
