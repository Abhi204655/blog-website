from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

blogs = [
    {
        'author': 'abhi' ,
        'title': 'Blog post 1',
        'content': 'first blog content',
        'datePosted': 'August 25, 2019'
    },
    {
        'author': 'amar',
        'title': 'Blog post 2',
        'content': 'second blog content',
        'datePosted': 'August 25, 2019'
    },
    {
        'author': 'divyendu',
        'title': 'Blog post 3',
        'content': 'third blog content',
        'datePosted': 'August 25, 2019'
    },
]
def home(request):
    context = {
        'blogs': blogs
    }
    return render(request,'home.html',context)
