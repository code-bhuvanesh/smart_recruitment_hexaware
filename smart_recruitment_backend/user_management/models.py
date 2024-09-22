from django.contrib.auth.models import User
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings

class CustomUser(AbstractUser):
    USER_TYPES = (
        ('recruiter', 'Recruiter'),
        ('applicant', 'Applicant'),
    )

    usertype = models.CharField(max_length=20, choices=USER_TYPES, default='applicant')

    def __str__(self):
        return f"{self.username} ({self.get_usertype_display()})"

class RecruiterProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    # company_name = models.CharField(max_length=100)
    # position = models.CharField(max_length=100)
    # Add more fields as needed

    def __str__(self):
        return self.user.username

class ApplicantProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    resume = models.FileField(upload_to='resumes/')
    skills = models.TextField()
    # Add more fields as needed

    def __str__(self):
        return self.user.username
