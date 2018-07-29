.PHONY: local image image-push

AUTHOR ?= samb1729
PROJECT := yamler
TAG ?= latest
IMAGE := $(AUTHOR)/$(PROJECT):$(TAG)

SOURCES := $(shell find . -type f -maxdepth 1 -name '*.py')

local: pipenv-installed
	pipenv install

pipenv-installed: python-installed
	@which pipenv > /dev/null \
		|| pip install pipenv

python-installed:
	@which python > /dev/null \
		|| (echo "python not installed" && exit 1)

image: $(SOURCES) Dockerfile .dockerignore
	docker build \
		-t $(IMAGE) \
		-f Dockerfile \
		.

image-push: image
	docker push $(IMAGE)
