D=docker
IMG=kiss

build:
	$(D) build -t $(IMG) .

run:
	$(D) run -it --rm \
	--mount src=$(shell pwd),target=/code,type=bind \
	$(IMG)

bash:
	$(D) run -it --rm \
	$(IMG) bash

bashmount:
	$(D) run -it --rm \
	--mount src=$(shell pwd),target=/code,type=bind \
	$(IMG) bash

new:
	python kiss/cli.py new example

clean:
	rm -rf example
