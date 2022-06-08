from django.db import models

from cloudinary.models import CloudinaryField

import instagram

class User(models.Model):
    name = models.CharField(max_length=40)
    pwd = models.CharField(max_length=40)

    def __str__(self):
        return self.name


class Profile(models.Model):
    name = models.CharField(max_length = 255,null=True)
    profile_pic= CloudinaryField('picture' ,null='True')
    bio = models.CharField(max_length = 255)

    def __str__(self):
        return self.name
     
    class Meta:
        ordering = ['name']

    def save_profile(self):
        self.save()

    @classmethod
    def search_by_name(cls,search_term):
        profile = cls.objects.filter(name__icontains=search_term)
        return profile


class Post(models.Model):
    picture =CloudinaryField('picture' ,null='True')
    caption = models.CharField(blank=True,max_length = 255)
    profile = models.ForeignKey(Profile,on_delete=models.CASCADE)
    like = models.IntegerField(default=0)
    comment = models.TextField(default=True)
    

    def __str__(self):
        return self.caption

class Followers(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    another_user = models.ManyToManyField(User, related_name='another_user')

    def __str__(self):
        return self.user.name

    def __str__(self):
        return self.name

class Comment(models.Model): 
    post = models.ForeignKey(Post,
                             on_delete=models.CASCADE,
                             related_name='comments')
    name = models.CharField(max_length=80)  
    body = models.TextField() 
    created = models.DateTimeField(auto_now_add=True) 
    updated = models.DateTimeField(auto_now=True) 
    active = models.BooleanField(default=True) 

    class Meta: 
        ordering = ('created',) 

    def __str__(self): 
        return 'Comment by {} on {}'.format(self.name, self.post) 
        

