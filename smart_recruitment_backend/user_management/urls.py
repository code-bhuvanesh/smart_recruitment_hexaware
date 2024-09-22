# user_management/urls.py

from django.urls import path
from .views import ApplicantSignupView, RecruiterSignupView, UserLoginView, PostedJobView

urlpatterns = [
    path('signup/applicant/', ApplicantSignupView.as_view(), name='applicant-signup'),
    path('signup/recruiter/', RecruiterSignupView.as_view(), name='recruiter-signup'),
    path('jobs/', PostedJobView.as_view(), name='recruiter-signup'),
    path('login/', UserLoginView.as_view(), name='user-login'),
]
