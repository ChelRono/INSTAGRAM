from django.test import TestCase
from .models import Profile,Post,Following,Comment

class ProfileTestClass(TestCase):

    # Set up method
    def setUp(self):
        self.valarie= Profile(name = 'valarie', bio ='Live.Love.Laugh')

    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.valarie,Profile))

        # Testing Save Method
    def test_save_method(self):
        self.valarie.save_profile()
        profile = Profile.objects.all()
        self.assertTrue(len(profile) > 0)

class PostTestClass(TestCase):

    def setUp(self):
        # Creating a new post and saving it
        self.valarie= Profile(name = 'valarie', bio ='Live.Love.Laugh')
        self.valarie.save_profile()

        # Creating a new comment and saving it
        self.new_comment = Comment(name = 'testing')
        self.new_comment.save()

        self.new_post= Post(caption = 'hey there',profile = 'valarie')
        self.new_post.save()

        self.new_post.comment.add(self.new_comment)

    def tearDown(self):
        Profile.objects.all().delete()
        Comment.objects.all().delete()
        Post.objects.all().delete()

class FollowingTestClass(TestCase):
    def setUp(self):
        self.sam=Following(name='sam',followed='valarie')
                            
    def test_instance(self):
        self.assertTrue(isinstance(self.sam,Following))

class CommentTestClass(TestCase):
    def setUp(self):
        self.first=Comment(post=1,
                            name='sam',
                            comment='nice picture',
                            date='May 20, 2018, 11:50 a.m.',
                            count=0)

    def test_instance(self):
        self.assertTrue(isinstance(self.first,Comment))

  
