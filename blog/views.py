from django.shortcuts import render


posts = [
    {
        'author': 'Dillon Hanni',
        'title': 'Blog Post 1',
        'content': 'First post content, written in Python!',
        'date_posted': 'February 29, 2020'
    },
    {
        'author': 'Richard Hanni',
        'title': 'Blog Post Number 2',
        'content': 'Second post content, this is awesome',
        'date_posted': 'February 28, 2020'
    }
]


def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html')
