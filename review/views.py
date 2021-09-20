from django.core.checks import messages
from review.models import Profile,Project,Users
from django.contrib.auth import authenticate, login,logout
from django.shortcuts import redirect, render
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
            user.save()
            messages.add_message(request,messages.SUCCESS, 'Account Created Succesfully!')
            return redirect('SignIn')
        else:
            print('Passwords do not match')

    return render(request,'auth/signup.html')

def SignIn(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(email=email,password=password)
        if user is not None:
            login(request, user)
            messages.add_message(request, messages.SUCCESS, "Logged in succesfully")
            return redirect('homepage')
        else:
            messages.add_message(request, messages.ERROR, "Sorry!")
        return redirect('SignIn')
            
    return render(request,'auth/login.html')

def signOut(request):
    logout(request)
    messages.add_message(request, messages.SUCCESS, "Successfully logged Out!")
    return redirect("SignIn") 