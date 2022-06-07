from django.contrib import admin
from .models import Profile,Post,Followers,Comment

admin.site.register(Profile)
admin.site.register(Post)
admin.site.register(Followers)
admin.site.register(Comment)
