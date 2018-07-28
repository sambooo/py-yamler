.PHONY: all image

AUTHOR ?= samb1729
PROJECT := yamler
TAG ?= latest
IMAGE := $(AUTHOR)/$(PROJECT):$(TAG)

SOURCES := $(shell find . -type f -maxdepth 1 -name '*.py')

all: image

image: $(SOURCES) Dockerfile .dockerignore
	docker build \
		-t $(IMAGE) \
		-f Dockerfile \
		.
