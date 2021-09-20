from django.db import models
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import BaseUserManager,AbstractBaseUser
# Create your models here.
c

class Profile(models.Model):
    user = models.OneToOneField('Users',on_delete = models.CASCADE)
    username = models.CharField(max_length=100,blank=True)
    email = models.EmailField(max_length=150)
    photo = CloudinaryField('prof',null=True,blank=True)
    signup_confirmation = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username','password']

    
