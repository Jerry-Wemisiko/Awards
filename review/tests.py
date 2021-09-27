from django.test import TestCase,TransactionTestCase
from django.contrib import auth
from .models import Profile, User,Project,Review

# Create your tests here
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

    def test_save_profile(self):
        self.profile.save_profile()
        profiles = Profile.objects.all()
        self.assertTrue(len(profiles) > 0)


    def test_delete_profile(self):
        self.profile.save_profile()
        self.profile.delete_profile()
        profile = Profile.objects.all()
        self.assertTrue(len(profile) == 0)       

class ProjectTest(TransactionTestCase):
    def setUp(self):
        self.project = Project(title ='ProjectIGI',url='https://localhost:8000',description="projectigi things")

    def tearDown(self):
        Project.objects.all().delete()

    def test_instance(self):
        self.assertTrue(isinstance(self.project, Project))

    def test_save_project(self):
        self.project.save_project()
        projects = Project.objects.all()
        self.assertTrue(len(projects)>0)

    def test_delete_project(self):
        self.project.save_project()
        projects = Project.objects.all()
        self.project.delete_project()
        projects = Project.objects.all()
        self.assertTrue(len(projects)==0)

# class ReviewTest(TestCase):
 
       
#     def setUp(self):
#         self.user = User(username='jerry')
#         self.user.save()
#         self.project = Project(title ='ProjectIGI',description="projectigi things",url="http://www.awards.net")
#         self.project.save_project()


#         self.new_review=Review(design="5",usability="5",content="5",user=self.user,project=self.project)
#         self.new_review.save_review()

#     def tearDown(self):
#         Review.objects.all().delete()

#     def test_instance(self):
#         self.assertTrue(isinstance(self.new_review,Review))

#     def test_save_review(self):
#         reviews = Review.objects.all()
#         self.assertTrue(len(reviews)>0)

#     def test_delete_review(self):
#         self.new_review.save_review()
#         self.new_review.delete_review()
#         reviews = Review.objects.all()
#         self.assertTrue(len(reviews)==0)