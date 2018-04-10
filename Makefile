.PHONY: all

all: local image

local:
	pyinstaller --onefile yamler.py

image:
	docker build -t yamler .
