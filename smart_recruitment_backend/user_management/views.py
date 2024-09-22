# accounts/views.py

from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from .models import RecruiterProfile, ApplicantProfile
from .serializers import RecruiterProfileSerializer, ApplicantProfileSerializer
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.response import Response

class RecruiterSignupView(generics.CreateAPIView):
    serializer_class = RecruiterProfileSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ApplicantSignupView(generics.CreateAPIView):
    serializer_class = ApplicantProfileSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginView(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        print("token")
        token, created = Token.objects.get_or_create(user=user)
        print(token)
        return Response({
            'token': token.key,
            'user_id': user.pk,
            # 'user_type': user.recruiterprofile if hasattr(user, 'recruiterprofile') else 'applicant'
        })