from django.db.models import fields
from  rest_framework import serializers
from .models import Profile,Project

class ProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = Profile
        fields = ('photo','bio','user')

class ProjectSerializer(serializers.ModelSerializer):

    class Meta:
        model = Project
        fields = ('title','description','url')