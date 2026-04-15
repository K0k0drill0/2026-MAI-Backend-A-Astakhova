.PHONY: build up down migrate createsuperuser logs

build:
	docker-compose build

up:
	docker-compose up -d

down:
	docker-compose down

migrate:
	docker-compose run --rm web python manage.py migrate

createsuperuser:
	docker-compose run --rm web python manage.py createsuperuser

logs:
	docker-compose logs -f
