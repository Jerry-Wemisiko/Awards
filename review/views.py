import review
from django.http.response import HttpResponseRedirect
from django.urls import reverse
from threading import current_thread
from django.contrib import auth
from review.forms import ReviewForm, SignUpForm,UserProfileForm,ProjectForm
from django.core.checks import messages
from review.models import Profile,Project, Review,User
from django.contrib.auth import authenticate, login,logout
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required

# Create your views here.
def homepage(request):

    title = 'Review'
    profile = Profile.objects.all()
    projects = Project.objects.all()
    reviews = Review.objects.all()

    return render(request,'index.html',{'profile':profile,'projects':projects,'title':title,'review': reviews})
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
    return render(request, 'new_project.html',{"form":form})

@login_required(login_url='/accounts/login')
def project(request,id):
    project = Project.objects.get(id=id)
    reviews = Review.objects.get(id=id)

    return render(request,'project.html',{'project':project,'reviews':reviews})

@login_required(login_url='/accounts/login/')
def project_review(request, proj_id):
    prj = Project.get_project_by_id(id=proj_id)
    project = get_object_or_404(Project,pk=proj_id)
    current_user = request.user

    if request.method == 'POST':
        form = ReviewForm(request.POST)

        if form.is_valid():
            design = form.cleaned_data['design']
            usability = form.cleaned_data['usability']
            content = form.cleaned_data['content']
            review = Review()
            review.user = current_user
            review.project = project
            review.content = content
            review.usability = usability
            review.design = design
            review.average = (review.content + review.usability + review.design)/3
            review.save()
            return HttpResponseRedirect(reverse('projectinfo', args=(project,)))

    else:
        form = ReviewForm()
    return render(request,'review.html',{'user':current_user,'form':form,'project':prj})





