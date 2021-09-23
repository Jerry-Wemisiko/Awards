from django.urls import path
from .import views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.homepage,name='homepage'),
    path('signup',views.SignUp,name='signup'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/',auth_views.LogoutView.as_view(), name='logout'),
    path('profile/', views.profile, name='profile'),
    path('project/',views.new_project,name='new_project'),
    path('projectinfo/',views.project, name='projectinfo'),
    path('review/', views.project_review,name='projectreview'),
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)