# accounts/serializers.py

from rest_framework import serializers
from django.contrib.auth.models import User
from .models import RecruiterProfile, ApplicantProfile

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user

class RecruiterProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = RecruiterProfile
        fields = ['user']

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user = UserSerializer.create(UserSerializer(), validated_data=user_data)
        recruiter_profile = RecruiterProfile.objects.create(user=user, **validated_data)
        return recruiter_profile

class ApplicantProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = ApplicantProfile
        fields = ['user', 'resume', 'skills']

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user = UserSerializer.create(UserSerializer(), validated_data=user_data)
        applicant_profile = ApplicantProfile.objects.create(user=user, **validated_data)
        return applicant_profile
