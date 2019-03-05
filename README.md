# django-blog-app

Learning django and python to build a blog app.

Note: A single project can contain multiple apps, which is good for separating out different part of project. You can take a single app and add it to multiple project.


## KEY POINTS

- create virtual environment
	pip list
	cd Desktop
	mkdir Djangoenv
	cd Djangoenv
	virtualenv project1_env
	project1_env\Scripts\activate   (linux: source project1_env/bin/activate)
	where python   (linux: which python)
	where pip
	
- install django
	pip install django
	python -m django --version
	django-admin startproject django_project
	cd django_project
	py manage.py runserver

- basic routing in django
  - create blog app within the project
	py manage.py startapp blog
```
|-- blog
|    |-- __init__.py
|    |-- admin.py
|    |-- apps.py
|    |-- migration
|    |    |-- __init__.py 
|    |-- models.py
|    |-- tests.py
|    |-- views.py
|-- db.sqlite3
|-- django_project
|    |-- __init__.py
|    |-- settings.py
|    |-- urls.py
|    |-- wsgi.py
|-- manage.py
```
  - add home & about page
