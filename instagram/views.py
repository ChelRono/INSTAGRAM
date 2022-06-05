from unicodedata import name
from django.shortcuts import render,redirect
from django.http  import HttpResponse
from .models import Profile,Post,Following,Comment

# Create your views here.
def index(request):

    

    return render(request, 'index.html')

def feed(request):
    posts = Post.objects.all()

    return render(request, 'feed.html',{"posts":posts})


