from django.test import TestCase
from django.contrib import auth
from .models import Profile, User,Project,Review

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
        self.profile = Profile(photo='img',bio='This is my bio',email='test@g.com',created_at='datefiled',user=self.user)
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

class ProjectTest(TestCase):
    def setUp(self):
        self.project = Project(title ='ProjectIGI',description="projectigi things",url="http://www.awards.net")

    def tearDown(self):
        Project.objects.all().delete()

    def test_instance(self):
        self.assertTrue(isinstance(self.project, Project))

    def test_save_method(self):
        self.project.save_project()
        projects = Project.objects.all()
        self.assertTrue(len(projects)>0)

    def test_delete_method(self):
        self.project.save_project()
        projects = Project.objects.all()
        self.project.delete_project()
        projects = Project.objects.all()
        self.assertTrue(len(projects)==0)

class ReviewTest(TestCase):
 
       
    def setUp(self):
        self.user = User(username='jerry')
        self.user.save()
        self.profile = Profile(photo='img',bio='This is my bio',email='test@g.com',created_at='datefiled',user=self.user)
        self.profile.save_project()


        self.new_review=Review(design="5",usability="5",content="5",user=self.user,project=self.project)
        self.new_review.save_review()

    def tearDown(self):
        Review.objects.all().delete()

    def test_instance(self):
        self.assertTrue(isinstance(self.new_review,Review))

    def test_save_review(self):
        reviews = Review.objects.all()
        self.assertTrue(len(reviews)>0)

    def test_delete_review(self):
        self.new_review.save_review()
        self.new_review.delete_review()
        reviews = Review.objects.all()
        self.assertTrue(len(reviews)==0)