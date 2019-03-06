# django-blog-app

Learning django and python to build a blog app.

Note: A single project can contain multiple apps, which is good for separating out different part of project. You can take a single app and add it to multiple project.


## KEY POINTS
__*create virtual environment*__
*	pip list
*	cd Desktop
*	mkdir Djangoenv
*	cd Djangoenv
*	virtualenv project1_env
*	project1_env\Scripts\activate   (linux: source project1_env/bin/activate)
*	where python   (linux: which python)
*	where pip
	
__*install django*__
*	pip install django
*	python -m django --version
*	django-admin startproject django_project
*	cd django_project
*	py manage.py runserver

__*basic routing in django*__
*	create blog app within the project
*	py manage.py startapp blog
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
*	add home & about page

__*use templates to return home and about page*__
*	do not forget to add the blog application to the list of installed apps in project's settings.py
*	blog.apps.BlogConfig
*	by adding apps to this list, django will correctly search the template
*	from django.shortcuts import render  (render function has the third optional arg, which will pass the data to the template
*	this third arg is a dict, the keys of the dict will be accessible in the template
