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
	 - py manage.py makemigrations
	 - py manage.py sqlmigrate blog 0001
	 - py manage.py migrate
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


__*user registration*__
*	py manage.py startapp users
*	in settings.py, add "'users.apps.UsersConfig'," to INSTALLED_APPS list
*	in users/views.py
```python
def register(request):
    form = UserCreationForm()
    return render(request, 'users/register.html', {'form': form})
```
*	create users/templates/users/register.html, which extends blog/base.html
*	in the form, we need to add "{% csrf_token %}", which is [Cross Site Request Forgery protection](https://docs.djangoproject.com/en/2.1/ref/csrf/)
*	in the project's url.py, create an url pattern that uses the register/views.py, so we can navigate to this page in the browser
	 - from users import views as user_views
	 - path('register/', user_views.register, name='register'),
*	if we get a POST request, it instantiates the UserCreationForm with that POST data, else eg. it's a GET request, we just desplay a blank form.
*	if the form is valid, create the user, save the data, grab the username, and redirect the user to the home page.
*	from django.contrib import messages, which has debug, info, success, warning and error tags.
```python
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('blog-home')
    else:
        form = UserCreationForm()
    return render(request, 'users/register.html', {'form': form})
```
*	put flush messages in base template so any massages pop up on any page.
```html
        <div class="col-md-8">
            {% if messages %}
                {% for message in messages %}
                    <div class="alert alert-{{ message.tags }}">
                        {{ message }}
                    </div>
                {% endfor%}
            {% endif %}
            {% block content %}{% endblock %}
        </div>
```

__*add email field to the form and use django-crispy-forms*__
*	users/forms.py
```python
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserRegisterForm(UserCreationForm):   # inheritsUserCreationForm
    email = forms.EmailField()              # default: required=True

    class Meta:                             # keep the configuration in one place
        model = User                        # the model that'll be affected is User model
        fields = ['username', 'email', 'password1', 'password2']  # fields will be shown in the model in this order
```
*	crispy forms allow us to put some simple tags in the template that'll style the form in a bootstrap fashion
*	pip install django-crispy-forms
*	in project/settings.py INSTALLED_APPS, add 'crispy_forms', CRISPY_TEMPLATE_PACK = 'bootstrap4'
*	in register.html
```
{% load crispy_forms_tags %}
{% block content %}
...
	{{ form|crispy }}
```

__*login/logout systems & users are forced to login before they can see the /profile page*__
*	in project/urls.py from django.contrib.auth import views as auth_views
*	create path: path('login/', auth_views.LoginViews.as_view(template_name='users/login.html'), name='login'),
*	LOGIN_REDIRECT_URL = 'blog-home'
*	modify register route to redirect users to login page:
	 - in users/views.py  f'Your account has been created! You are now able to log in'
	 - return redirect('login')
*	django provides a user variable that contains the current user and has an attribute called .is_authenticated to check if the user is currently logged in


__*create user's profile page that users can access after logged in*__
*	create the view: in users/views.py
```python
def profile(request):
    return render(request, 'users/profile.html')
```
*	create the template: users/templates/users/profile.html
*	create the routes in url_patterns that will use this view: in urls.py urlpatterns list, add path('profile/', user_views.profile, name='profile'),
*	add profile button in navigation bar in base.html, display a link to the profile page when logged in
*	put a check to see if the user is logged in before accessing the profile page:
	 - in views.py, from django.contrib.auth.decorators import login_required
```python
@login_required
def profile(request):
    return render(request, 'users/profile.html')
```
*	.../accounts/login/?next=/profile/ is the default location that django looks for login routes, but we have simply put our login page at /login, so we need to tell django where it can find the login route:
	 - in settings.py LOGIN_URL = 'login'
*	?next=/profile/ it's keeping track of the page that we were trying to access and it will direct us to that page after we log in
	 - note: the default redirect url is to the 'home-page'
	 - so if we log in here, we will be redirected to /profile page now


__*user's profile and picture*__
*	extend the existing User model that django provides
*	in users/models.py
```python
from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'
```
*	Anytime after changing the models, be sure to makemigrations to update the database
*	pip install Pillow
*	py manages.py makemigrations
*	py manages.py migrate
*	in order to be able to view the profile on /admin page, we need to register this model within admin.py
*	in users/admin.py:
```python
from django.contrib import admin
from .models import Profile

admin.site.register(Profile)
```
*	add profile manually through admin page
```
(PROJEC~1) C:\Users\Jiayi Su\Desktop\Djangoenv\django_project>py manage.py shell
Python 3.7.2 (tags/v3.7.2:9a3ffc0492, Dec 23 2018, 23:09:28) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
(InteractiveConsole)
>>> from django.contrib.auth.models import User
>>> user = User.objects.filter(username='jiayisu').first()
>>> user
<User: jiayisu>
>>> user.profile
<Profile: jiayisu Profile>
>>> user.profile.image
<ImageFieldFile: profile_pics/girl.jpg>
>>> user.profile.image.width
564
>>> user.profile.image.url
'profile_pics/girl.jpg'
>>> user = User.objects.filter(username='TestUser').first()
>>> user
<User: TestUser>
>>> user.profile.image
Traceback (most recent call last):
  File "<console>", line 1, in <module>
  File "C:\Users\JIAYIS~1\Desktop\DJANGO~1\PROJEC~1\lib\site-packages\django\db\models\fields\related
_descriptors.py", line 414, in __get__
    self.related.get_accessor_name()
django.contrib.auth.models.User.profile.RelatedObjectDoesNotExist: User has no profile.
>>>
```

*	change the dir where the profile pictures will be saved
	 - in settings.py:  MEDIA_ROOT = os.path.join(BASE_DIR, 'media')   MEDIA_URL = '/media/'
*	profile.html
```html
{% extends "blog/base.html" %}
{% load crispy_forms_tags %}
{% block content %}
    <div class="content-section">
      <div class="media">
        <img class="rounded-circle account-img" src="{{ user.profile.image.url }}">
        <div class="media-body">
          <h2 class="account-heading">{{ user.username }}</h2>
          <p class="text-secondary">{{ user.email }}</p>
        </div>
      </div>
      <!-- FORM HERE -->
    </div>
{% endblock content %}
```
*	[Serving files uploaded by a user during development](https://docs.djangoproject.com/en/2.1/howto/static-files/#serving-files-uploaded-by-a-user-during-development)
*	During development, you can serve user-uploaded media files from MEDIA_ROOT using the django.views.static.serve() view.This is not suitable for production use! 
*	in project/urls.py
```python
from django.conf import settings
from django.conf.urls.static import static

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```
*	auto-set default pic for newly-created users
	 - in users/signals.py
```python
from django.db.models.signals import post_save        # signal
from django.contrib.auth.models import User           # sender
from django.dispatch import receiver
from .models import Profile


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()
```

*	import the signal inside of the ready function of users/apps.py
```python
from django.apps import AppConfig


class UsersConfig(AppConfig):
    name = 'users'

    def ready(self):
        import users.signals
```

__*update user's profile (information and picture) and auto-resize uploaded picture*__
*	users/forms.py create a model form, which allows us to create a form that'll work with a specific database model.
*	here, we want our form to update the user model

```python
class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']
```
*	add these forms to profile view
```python
@login_required
def profile(request):
    u_form = UserUpdateForm()
    p_form = ProfileUpdateForm()
    
    context = {
        'u_form': u_form,
        'p_form': p_form,
    }

    return render(request, 'users/profile.html', context)
```

*	put two fields for these forms into a single form, so the user see it as one
*	in users/profile.html
```html
<!-- FORM HERE IS USERUPDATE & PROFILEUPDATE Form-->
      <form method="POST" enctype="multipart/form-data">
        {% csrf_token %}
        <fieldset class="form-group">
            <legend class="border-bottom mb-4">Profile Info</legend>
            {{ u_form|crispy }}
            {{ p_form|crispy }}
        </fieldset>
        <div class="form-group">
            <button class="btn btn-outline-info" type="submit">Update</button>
        </div>
      </form>
```

*	populate the fields with current user info: in views.py
```python
@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES,
                                   instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request,
                             f'Your account has been updated!')
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form,
    }

    return render(request, 'users/profile.html', context)
```

*	auto-resize image when uploading picture: in models.py, override the save method
```python
    def save(self):
        super().save()

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)
```

*	display the image of the author beside each post: blog/home.html
```html
   <img class="rounded-circle article-img" src="{{ post.author.profile.image.url }}">
```

__*function view VS class-based view*__
*	ListView, DetailView, CreateView, UpdateView, DeleteView
*	in blog/views.py, create a ListView for model Post. We can change the template django was looking for with template_name
*	in blog/urls.py:
```python
from .views import PostListView

urlpatterns = [
    # path('', views.home, name='blog-home'),
    path('', PostListView.as_view(), name='blog-home'),
    path('about/', views.about, name='blog-about'),
]
```

*	by default, ListView will call the variable object_list instead of posts, so we can either go into the template and change it so it's looping over object_list
*	or we can set one more variable in our ListView and let the class know that we want that variable to be called "posts" instead
*	to see the latest post at the top, we need to change the order our query is making to the database:
	 - in our ListView, add an ordering attribute with the field we want to order on, the minus sign will reverse the order
```python
from django.views.generic import ListView

# ------------function view
def home(request):
    context = {
        'posts': Post.objects.all()
    }
    # return HttpResponse('<h1>Blog Home</h1>')
    return render(request, 'blog/home.html', context)

# ------------class-based view
class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'    # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date_posted']
```

__*a detail view: a view for individual post*__
*	views.py
```python
class PostDetailView(DetailView):
    model = Post
```

*	urls.py: pk is the primary key of the post we want to view, pk will be passed to the class-based view
```python
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
```

*	create a template that'll desplay our post details
	 - in views, by default, our generic class-based view will be looking for a template with the naming convention: <app>/<model>_<viewtype>.html
	 - so we need to create a template: blog/templates/blog/post_detail.html 
	 - within this html, change "post" to "object"
*	now we can add links to the routes for the individual post on the home page:
	 - home.html
```html
<h2><a class="article-title" href="{% url 'post-detail' post.id %}">{{ post.title }}</a></h2>
```



