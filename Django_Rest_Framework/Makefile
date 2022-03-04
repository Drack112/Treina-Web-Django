format:
	black ./*.py && black ./*/*.py && black ./*/*/*.py

migrations:
	python manage.py makemigrations

migrate:
	python manage.py migrate

mixer:
	python manage.py shell < api/mixer/mixer.py

dumpdata:
	python manage.py dumpdata --format json > dados.json

loaddata:
	python manage.py loaddata dados.json

clear_db:
	python manage.py flush

create_cache:
	python manage.py createcachetable

runserver:
	python manage.py runserver	