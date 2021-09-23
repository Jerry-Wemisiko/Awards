from django.db.models import fields
from review.models import Profile,Project
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class SignUpForm(UserCreationForm):
     email = forms.EmailField(max_length=300)

     class Meta:
        model = User
        fields = ('username','email','password1','password2')
class UserProfileForm(forms.ModelForm):
   
    class Meta:
        model = Profile
        fields = ['user', 'photo','bio',]

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        exclude = ['user','profile']