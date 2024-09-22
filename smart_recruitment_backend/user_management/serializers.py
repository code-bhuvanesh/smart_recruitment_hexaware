# user_management/serializers.py

from datetime import timezone
from rest_framework import serializers
from .models import CustomUser, Applicant, Recruiter, PostedJob
from django.contrib.auth import authenticate

class ApplicantSignupSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['username', 'password', 'email', 'usertype']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = CustomUser(
            username=validated_data['username'],
            email=validated_data['email'],
            usertype='applicant'
        )
        user.set_password(validated_data['password'])
        user.save()
        applicant = Applicant.objects.create(user=user, skills=validated_data.get('skills', ''))
        return user


class RecruiterSignupSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['username', 'password', 'email', 'usertype']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = CustomUser(
            username=validated_data['username'],
            email=validated_data['email'],
            usertype='recruiter'
        )
        user.set_password(validated_data['password'])
        user.save()
        recruiter = Recruiter.objects.create(user=user, company_name=validated_data.get('company_name', ''))
        return user


class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, attrs):
        username = attrs.get('username')
        password = attrs.get('password')

        if username and password:
            user = authenticate(username=username, password=password)
            if user is None:
                raise serializers.ValidationError("Invalid credentials.")
        else:
            raise serializers.ValidationError("Must include username and password.")
        
        attrs['user'] = user
        return attrs



class PostedJobSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostedJob
        fields = [
            'user',  # Include user field
            'job_location',
            'employment_type',
            'salary_range',
            'application_deadline',
            'required_qualifications',
            'preferred_qualifications',
            'responsibilities'
        ]
        read_only_fields = ('user',)  # Prevent users from setting this field

    def create(self, validated_data):
        user = validated_data.pop('user')  # Extract user info
        job = PostedJob.objects.create(user=user, **validated_data)
        return job
    
    def validate_application_deadline(self, value):
        if value < timezone.now().date():
            raise serializers.ValidationError("Application deadline must be a future date.")
        return value

    def validate_salary_range(self, value):
        if not value.replace('.', '', 1).isdigit():
            raise serializers.ValidationError("Salary range must be numeric values.")
        return value
