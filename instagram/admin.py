from django.contrib import admin
from .models import Profile,Post,Followers,Comment


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'post', 'created', 'active')
    list_filter = ('active', 'created', 'updated')
    search_fields = ('name', 'body')

admin.site.register(Profile)
admin.site.register(Post)
admin.site.register(Followers)

