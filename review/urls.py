from django.conf.urls import url
from .import views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url('$',views.homepage,name='homepage'),
    url('register/',views.SignUp,name='registration'),
    url('login/', auth_views.LoginView.as_view(), name='login'),
    url('logout/',auth_views.LogoutView.as_view(), name='logout'),
    url('profile/', views.profile, name='profile'),
    url('post_project/',views.new_project,name='new_project'),
    url('^projectinfo/(?P<id>\d+)',views.project, name='projectinfo'),
    url('^review/(?P<proj_id>\d+)', views.project_review,name='projectreview'),
     url('api/projects',views.ProjectList.as_view(),name='projectapi'),
    url('api/profiles',views.ProfileList.as_view(),name='profileapi'),
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)