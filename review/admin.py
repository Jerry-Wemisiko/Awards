from django.contrib import admin
from django.db import models
from review.models import Profile,Project,Review
# Register your models here.
admin.site.register(Profile)
admin.site.register(Project)
admin.site.register(Review)
