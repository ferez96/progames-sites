runserver:
	python manage.py runserver

lint:
	DJANGO_SETTINGS_MODULE=admin.settings pylint --load-plugins pylint_django admin polls
