export SHELL:=/bin/bash
export SHELLOPTS:=$(if $(SHELLOPTS),$(SHELLOPTS):)pipefail:errexit

.ONESHELL:

create_db:
	source .env

	docker-compose down
	docker-compose up -d

	sleep 10

	python create_tables.py