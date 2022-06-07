from django.urls import re_path as  url
from . import views


urlpatterns = [
url(r'^$',views.index,name = 'index'),
url(r'^feed/', views.feed, name = 'feed'),
url(r'^search/', views.search_results, name='search_results'),
url(r'^profile/',views.profile,name ='profile'),
url("register", views.register_request, name="register"),
url("login", views.login_request, name="login"),
url("logout", views.logout_request, name= "logout"),



]