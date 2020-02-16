from django.shortcuts import render
from django.http import HttpResponse
from .models import posts
from django.contrib.auth.models import User

# Create your views here.

def home(request):
    context = {
        'blogs': posts.objects.all()
    }
    return render(request,'home.html',context)


def profile(request):
    context = {
        'blogs': posts.objects.filter(username = User.username)
    }
    return render(request, 'profile.html',context)
