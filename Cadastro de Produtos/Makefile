migrations:
	python manage.py makemigrations

migrate:
	python manage.py migrate

clear_db:
	python manage.py flush

dumpdata:
	python manage.py dumpdata --format json > dados.json

loaddata:
	python manage.py loaddata dados.json

runserver:
	python manage.py runserver	

format:
	black ./*.py && black ./*/*.py && black ./*/*/*.py

mixer_cliente:
	python manage.py shell < clientes/mixers/clientes_mixer.py	

create_cache:
	python manage.py createcachetable