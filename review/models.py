from django.db import models
from django.db.models.fields import URLField
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    user=models.OneToOneField(User,on_delete = models.CASCADE, related_name='profile',primary_key=True)
    username = models.CharField(max_length=100,blank=True)
    bio = models.TextField()
    email = models.EmailField(max_length=150)
    photo = CloudinaryField('prof',null=True,blank=True)
    signup_confirmation = models.BooleanField(default=False)

    def __str__(self) ->str:
        return self.user.username
    
    def save_profile(self):
        self.save()

    def delete_profile(self):
        self.delete()

    @classmethod
    def search_profile(cls,uname):
        return cls.objects.filter(user__username__icontains=uname).all()

class Project(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    url = URLField(max_length=255)
    description = models.TextField()
    # upload_date = models.DateTimeField(auto_now_add=True)
    profile = models.ForeignKey(Profile,null=True,on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.title

    def save_project(self):
        self.save()

    def delete_project(self):
        self.delete()

    @classmethod
    def get_project_by_id(cls,id):
        project = Project.objects.filter(id =id)
        return project

    @classmethod
    def search_project(cls,proj_title):
      projects=cls.objects.filter(title__icontains=proj_title)
      return projects

class Review(models.Model):
    CHOICES = (
        (1,'1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
        (6, '6'),
        (7, '7'),
        (8, '8'),
        (9, '9'),
        (10, '10'),
    )
    design = models.IntegerField(choices=CHOICES,default=0,blank=False)
    usability = models.IntegerField(choices=CHOICES,default=0,blank=False)
    content = models.IntegerField(choices=CHOICES,default=0,blank=False)
    average =  models.DecimalField(default=1,blank=False,decimal_places=2,max_digits=100)
    project = models.ForeignKey(Project,null=True,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.user

    def save_review(self):
        self.save()

    def delete_review(self):
        self.delete()
