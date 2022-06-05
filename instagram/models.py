from django.db import models

from cloudinary.models import CloudinaryField

class Profile(models.Model):
    name = models.CharField(max_length = 255,null=True)
    profile_pic= CloudinaryField('picture' ,null='True')
    bio = models.CharField(max_length = 255)

    def __str__(self):
        return self.name
     
    class Meta:
        ordering = ['name']

class Post(models.Model):
    picture =CloudinaryField('picture' ,null='True')
    caption = models.CharField(blank=True,max_length = 255)
    profile = models.ForeignKey(Profile,on_delete=models.CASCADE)
    like = models.IntegerField(default=0)
    

    def __str__(self):
        return self.caption

class Following(models.Model):
    name = models.CharField(blank=True,max_length = 255)
    followed = models.CharField(blank=True,max_length = 255)

    def __str__(self):
        return self.name

class Comment(models.Model):
    post = models.IntegerField(default=0)
    name = models.CharField(blank=True,max_length = 255)
    comment = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    count = models.IntegerField(default=0)

    def __str__(self):
        return self.name
        

