from review.models import Profile,Project,Users
from django.shortcuts import render
from django.contrib.auth.hashers import make_password

# Create your views here.
def homepage(request):
    title = 'Review'
    profile = Profile.objects.all()
    projects = Project.objects.all()

    return render(request,'index.html',{'title':title,'profile':profile,'projects':projects})

def SignUp(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        if password == confirm_password:
            user= Users(username=username, email =email,password=make_password(password))
        else:
            return('Passwords do not match')
    return render(request,'auth/signup.html')