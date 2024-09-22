# accounts/urls.py

from django.urls import path
from .views import RecruiterSignupView, ApplicantSignupView, LoginView

urlpatterns = [
    path('signup/recruiter/', RecruiterSignupView.as_view(), name='signup_recruiter'),
    path('signup/applicant/', ApplicantSignupView.as_view(), name='signup_applicant'),
    path('login/', LoginView.as_view(), name='login'),
]
