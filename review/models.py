from django.db import models
from django.db.models.fields import URLField
from cloudinary.models import CloudinaryField
import datetime as dt
from django.contrib.auth.models import User, BaseUserManager,AbstractBaseUser

# Create your models here.
class MyAccountManager(BaseUserManager):
    def create_user(self,email,username,password=None):
        if not email:
            raise ValueError("User must have an email address")
        if not username:
            raise ValueError("User must have a username")

        user = self.model(
            email=self.normalize_email(email),
            username=username,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self,email,username,password):
        user = self.self.create_user(
            email=self.normalize_email(email),
            password=password,
            username=username
        )
        user.email = email
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

class Users(AbstractBaseUser):
    username = models.CharField( max_length=20, unique=True)  
    email = models.CharField( max_length=50, unique=True)
    name = models.CharField( max_length=50, unique=False)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    password = models.CharField( max_length=100)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username','password']

    objects=MyAccountManager()
     
    def _str_(self):
        return self.email
    
    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True


class Profile(models.Model):
    user = models.OneToOneField('Users',on_delete = models.CASCADE)
    username = models.CharField(max_length=100,blank=True)
    bio = models.TextField()
    email = models.EmailField(max_length=150)
    photo = CloudinaryField('prof',null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    signup_confirmation = models.BooleanField(default=False)

    def __str__(self) ->str:
        return f'{self.user.username}'
    
    def save_profile(self):
        self.user.save()

    @classmethod
    def search_profile(cls,uname):
        return cls.objects.filter(user__username__icontains=uname).all()

class Project(models.Model):
    user = models.ForeignKey('Users',on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    url = URLField(max_length=255)
    description = models.TextField()
    upload_date = models.DateTimeField(auto_now_add=True)
    profile = models.ForeignKey(Profile,null=True,on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.title

    class Meta:
        ordering = ['upload_date']

    def save_project(self):
        return self.save()

    @classmethod
    def get_project_by_id(cls,id):
        project = Project.objects.filter(id =id)
        return project

    @classmethod
    def delete_project(cls,id):
      cls.objects.filter(id=id).delete()


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
    user = models.ForeignKey('Users',null=True,blank=True,on_delete=models.CASCADE)

    def __str__(self):
        return self.user

    def save_review(self):
        self.save()

    def delete_review(self):
        self.delete()

    