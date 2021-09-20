from review.models import Profile
from django.shortcuts import render

# Create your views here.
def homepage(request):
    title = 'Review'
    profile = Profile.objects.all()
    projects = Project.objects.all()

    return render(request,'index.html',{'title':title,'profile':profile,'projects':projects})