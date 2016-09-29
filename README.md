# django-multi-instances
Django project structured to work with multiple instances

## makemigrations
- python manage.py makemigrations --settings=settings.proj1
- python manage.py makemigrations --settings=settings.proj2

## migrate
- python manage.py migrate --settings=settings.proj1
- python manage.py migrate --settings=settings.proj2

## run django development server
- python manage.py runserver 0.0.0.0:8001 --settings=settings.proj1
- python manage.py runserver 0.0.0.0:8002 --settings=settings.proj2