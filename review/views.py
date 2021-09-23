from threading import current_thread
from django.contrib import auth
from review.forms import SignUpForm,UserProfileForm,ProjectForm
from django.core.checks import messages
from review.models import Profile,Project,Users
from django.contrib.auth import authenticate, login,logout
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required

# Create your views here.
def homepage(request):
    title = 'Review'
    profile = Profile.objects.all()
    projects = Project.objects.all()

def SignUp(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username,password=raw_password)
            login(request, user)
            return redirect('login')

        else:
            form = SignUpForm()
        return render(request,'auth/signup.html',{'form': form})
        
@login_required(login_url='/accounts/login/')    
def profile(request):
    if request.method == 'POST':
        profile_form = UserProfileForm(request.POST, request.FILES, instance=request.user)
        if  profile_form.is_valid():
            profile_form.save()
            return redirect('homepage')
    else:
        profile_form = UserProfileForm(instance=request.user)
    return render(request, 'profile.html',{ "profile_form": profile_form})

@login_required(login_url='/accounts/login')
def new_project(request):
    current_user = request.user
    if request.method == 'POST':
        form = ProjectForm(request.POST,request.FILES)
        if form.is_valid():
            new_project = form.save(commit=False)
            new_project.user = current_user
            new_project.save()
            return redirect('homepage')
    else:
        form = ProjectForm()
    return render(request, 'project.html',{"form":form})

@login_required(login_url='/accounts/login')
def project(request):
    project = Project.objects.get.all()
    reviews = Rev
