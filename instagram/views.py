from unicodedata import name
from django.shortcuts import render,redirect,get_object_or_404
from django.http  import HttpResponse,Http404
from .models import Profile,Post,Followers,Comment
from django.core.exceptions import ObjectDoesNotExist
from .forms import NewUserForm
from django.contrib.auth import login,authenticate,logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from .forms import PostForm,CommentForm
from .models import Post

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

def profile(request):
   profiles = Profile.objects.all()
     
   return render(request,"profile.html", {"profiles":profiles})


def register_request(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
    
			messages.success(request, "Registration successful." )
			return redirect('accounts/login')
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = NewUserForm()
	return render (request=request, template_name="registration/registration_form.html", context={"register_form":form})

def login_request(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.info(request, f"You are now logged in as {username}.")
				return redirect('feed')
			else:
				messages.error(request,"Invalid username or password.")
		else:
			messages.error(request,"Invalid username or password.")
	form = AuthenticationForm()
	return render(request=request, template_name="registration/login.html", context={"login_form":form})

def logout_request(request):
	logout(request)
	messages.info(request, "You have successfully logged out.") 
	return redirect("index")


def add_post(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = Post()
            post.image_caption = request.POST.get('image_caption')
            post.save()
            return redirect('feed')
			
    else:
        form = PostForm()

    return render(request, 'add-post.html', {'form': form})

def post_detail(request):
    template_name = 'post_detail.html'
    post = Post()
    comments = CommentForm()
    new_comment = None
    # Comment posted
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():

            # Create Comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
            new_comment.post = post
            # Save the comment to the database
            new_comment.save()
    else:
        comment_form = CommentForm()

    return render(request, template_name, {'post': post,
                                           'comments': comments,
                                           'new_comment': new_comment,
                                           'comment_form': comment_form})

def followers(request):

	return render(request)

def follow_user(request):

	return render (request)
