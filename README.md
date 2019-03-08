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


__*template inheritance*__
*	base.html contains repeated section of home and about templates.
*	add bootstrap to the website
*	add navigation bar, beautify content, custom styles in main.css
*	[Starter template](https://getbootstrap.com/docs/4.0/getting-started/introduction/#starter-template)
*	in Django, static files (eg. css and javascripte) need to be located in a static directory within the blog app
*	use Django url tag with the name of the route in urlpattern instead of hard-coding it for better maintainess


__*create database & migrations & query data*__
*	Django ORM, Object-Relational Mapping, is a technique that lets you query and manipulate data from a database using an object-oriented paradigm
*	Django ORM represent database structure as classes(models)
*	each class is its own table in the database, each attribute of the class is a field in the database
*	author is user, which is a separate table
*	from django.contrib.auth.models import User
*	author = models.ForeignKey(User, on_delete=models.CASCADE)   # if user is deleted, post also
*	we need to run migrations to update the database with any change
*	 - py manage.py makemigrations
*	 - py manage.py sqlmigrate blog 0001
*	 - py manage.py migrate
*	Django python shell allow us to work with the models interactively line by line:
	 - py manage.py shell
```
(PROJEC~1) C:\Users\Jiayi Su\Desktop\Djangoenv\django_project>py manage.py makemigrations
Migrations for 'blog':
  blog\migrations\0001_initial.py
    - Create model Post

(PROJEC~1) C:\Users\Jiayi Su\Desktop\Djangoenv\django_project>py manage.py sqlmigrate blog 0001
BEGIN;
--
-- Create model Post
--
CREATE TABLE "blog_post" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "title" varchar(100) NOT N
ULL, "content" text NOT NULL, "date_posted" datetime NOT NULL, "author_id" integer NOT NULL REFERENCE
S "auth_user" ("id") DEFERRABLE INITIALLY DEFERRED);
CREATE INDEX "blog_post_author_id_dd7a8485" ON "blog_post" ("author_id");
COMMIT;

(PROJEC~1) C:\Users\Jiayi Su\Desktop\Djangoenv\django_project>py manage.py migrate
Operations to perform:
  Apply all migrations: admin, auth, blog, contenttypes, sessions
Running migrations:
  Applying blog.0001_initial... OK



(PROJEC~1) C:\Users\Jiayi Su\Desktop\Djangoenv\django_project>py manage.py shell
Python 3.7.2 (tags/v3.7.2:9a3ffc0492, Dec 23 2018, 23:09:28) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
(InteractiveConsole)
>>> from blog.models import Post
>>> from django.contrib.auth.models import User
>>> User.objects.all()
<QuerySet [<User: jiayisu>, <User: TestUser>]>
>>> User.objects.first()
<User: jiayisu>
>>> User.objects.filter(username='jiayisu')
<QuerySet [<User: jiayisu>]>
>>> User.objects.filter(username='jiayisu').first()
<User: jiayisu>
>>> user = User.objects.filter(username='jiayisu').first()
>>> user
<User: jiayisu>
>>> user.id
1
>>> user.pk
1
>>> user = User.objects.get(id=1)
>>> user
<User: jiayisu>
>>> Post.objects.all()
<QuerySet []>
>>> post_1=Post(title='Blog 1', content='First Post Content!', author=user)
>>> Post.objects.all()
<QuerySet []>
>>> post_1.save()
>>> Post.objects.all()
<QuerySet [<Post: Post object (1)>]>
>>> exit()


    def __str__(self):
        return self.title

(PROJEC~1) C:\Users\Jiayi Su\Desktop\Djangoenv\django_project>py manage.py shell
Python 3.7.2 (tags/v3.7.2:9a3ffc0492, Dec 23 2018, 23:09:28) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
(InteractiveConsole)
>>> from blog.models import Post
>>> from django.contrib.auth.models import User
>>> Post.objects.all()
<QuerySet [<Post: Blog 1>]>
>>> User.objects.filter(username='jiayisu').first()
<User: jiayisu>
>>> user = User.objects.filter(username='jiayisu').first()
>>> user
<User: jiayisu>
>>> post_2 = Post(title='Blog 2', content='Second Post Content!', author_id=user.id)
>>> post_2.save()
>>> Post.objects.all()
<QuerySet [<Post: Blog 1>, <Post: Blog 2>]>
>>> post = Post.objects.first()
>>> post.content
'First Post Content!'
>>> post.date_posted
datetime.datetime(2019, 3, 7, 22, 23, 49, 609491, tzinfo=<UTC>)
>>> post.author
<User: jiayisu>
>>> post.author.email
'sujiayi317@gmail.com'

>>> #--------------------------get all the post by this user-------------------------------------------
>>> user.post_set
<django.db.models.fields.related_descriptors.create_reverse_many_to_one_manager.<locals>.RelatedManag
er object at 0x000001A0F67EAB00>
>>> user.post_set.all()
<QuerySet [<Post: Blog 1>, <Post: Blog 2>]>
>>> #--------------------------create a post directly (no need to specify user & save)------------------
>>> user.post_set.create(title='Blog 3', content='Third Post Content!')
<Post: Blog 3>
>>> Post.objects.all()
<QuerySet [<Post: Blog 1>, <Post: Blog 2>, <Post: Blog 3>]>
>>>
```

__*query the data and pass it to view.py*__
*	from .models import Post      # use the post from database
*	'post':Post.objects.all()     # query the posts
*	py manage.py runserver        # now, the posts are updated
*	change the formatting of the date_posted: in home.html, post.date_posted(date:"F d, Y")
	 - [Formats a date according to the given format](https://docs.djangoproject.com/en/2.1/ref/templates/builtins/)
*	to see Post model in admin page, we have to register Post in admin.py
	 - from .models import Post
	 - admin.site.register(Post)
*	now we can update, delete, change author of any post
