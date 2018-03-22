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
	--mount src=$(shell pwd)/example,target=/example,type=bind \
	$(IMG) bash

bashmount:
	$(D) run -it --rm \
	--mount src=$(shell pwd),target=/code,type=bind \
	$(IMG) bash
