from django.test import TestCase
from django.contrib import auth
from .models import Profile, User

# Create your tests here.


# class AuthTestCase(TestCase):
#     def setUp(self):
#         self.user = User.objects.create_user('test@dom.com', 'test@dom.com', 'pass')
#         self.user.is_staff = True
#         self.user.is_superuser = True
#         self.user.is_active = True
#         self.user.save()

#     def testLogin(self):
#         self.client.login(username='test@dom.com', password='pass')

class ProfileTest(TestCase):
    def setUp(self):
        self.user = User(username='jerry')
        self.user.save()
        self.profile = Profile(photo='img',bio='This is my bio',email='test@g.com',user=self.user)
        self.profile.save_profile()

    def tearDown(self):
        Profile.objects.all().delete()

    def test_instance(self):
        self.assertTrue(isinstance(self.profile,Profile))

    def test_save_method(self):
        self.profile.save_profile()
        profiles = Profile.objects.all()
        self.assertTrue(len(profiles) > 0)


    def test_delete_method(self):
        self.profile.save_profile()
        self.profile.delete_profile()
        profile = Profile.objects.all()
        self.assertTrue(len(profile) == 0)       
