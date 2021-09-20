from django.urls import path
from .import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('home',views.homepage,name='homepage'),
    path('',views.SignUp,name='signup'),
    path('signin',views.SignIn,name='signin'),
    path('signout',views.signOut,name='signout'),
]