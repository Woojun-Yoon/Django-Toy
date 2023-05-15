# Django-Toy Project

## A. Start Project
1. Create virtual env
2. Create Project and App
3. install requirements

## B. Build Project
1. Implement board function
2. Mapping DB(sqlite3)
3. Implement login, logout, signup system
4. Fix bugs(auth policy, UI)

# How to Start?
python -m venv Toyenv
-> Make virtualenv

source Toyenv/bin/activate
-> Run virtualenv

deactivate
-> terminate virtualenv

django-admin startproject "Project name"
-> Create Project

python manage.py runserver
-> Run Server 

django-admin startapp "App name"
-> Create App

python manage.py makemigrations
-> Make migrations

python manage.py migrate
-> Do migrate

python manage.py createsuperuser
-> Create SuperUser