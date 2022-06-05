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

  
