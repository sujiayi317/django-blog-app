from django.shortcuts import render
# from django.http import HttpResponse

posts = [
    {
        'author': 'Beiguang',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'March 3, 2019'
    },
    {
        'author': 'Jiayi',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'March 4, 2019'
    }
]


# Create your views here.
def home(request):
    context = {
        'posts': posts
    }
    # return HttpResponse('<h1>Blog Home</h1>')
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
