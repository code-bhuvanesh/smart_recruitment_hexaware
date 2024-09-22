from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.utils import timezone

class CustomUser(AbstractUser):
    USER_TYPES = (
        ('recruiter', 'Recruiter'),
        ('applicant', 'Applicant'),
    )
    usertype = models.CharField(max_length=20, choices=USER_TYPES, default='applicant')

    def __str__(self):
        return self.username


class Applicant(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    skills = models.CharField(max_length=255)  # Add skills as a comma-separated string or a more complex structure
    additional_info = models.TextField(blank=True)  # Add fields as needed

    def __str__(self):
        return self.user.username


class Recruiter(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=255)
    additional_info = models.TextField(blank=True)  # Add fields as needed

    def __str__(self):
        return self.user.username


class PostedJob(models.Model):
    EMPLOYMENT_TYPES = [
        ('full_time', 'Full-time'),
        ('part_time', 'Part-time'),
        ('contract', 'Contract'),
        ('internship', 'Internship'),
    ]
    
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)  # Link to the user
    job_location = models.CharField(max_length=255)
    employment_type = models.CharField(max_length=20, choices=EMPLOYMENT_TYPES)
    salary_range = models.CharField(max_length=50)
    application_deadline = models.DateField()
    required_qualifications = models.TextField()
    preferred_qualifications = models.TextField(blank=True)
    responsibilities = models.TextField()

    def __str__(self):
        return f"{self.job_location} - {self.employment_type}"