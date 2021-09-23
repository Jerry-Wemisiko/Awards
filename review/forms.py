from django.db.models import fields
from review.models import Profile,Project, Review
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class SignUpForm(UserCreationForm):
     email = forms.EmailField(max_length=250)

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

class ReviewForm(forms.ModelForm):

    class Meta:
        model = Review
        exclude = ['user','project','average']
