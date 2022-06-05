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

def search_results(request):

    if 'profile' in request.GET and request.GET["profile"]:
        search_term = request.GET.get("profile")
        searched_profile = Profile.search_by_name(search_term)
        message = f"{search_term}"

        return render(request, 'search.html',{"message":message,"profile": searched_profile})

    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html',{"message":message})


