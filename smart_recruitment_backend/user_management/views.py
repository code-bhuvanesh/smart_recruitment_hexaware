# user_management/views.py

from rest_framework import generics
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from .models import CustomUser, PostedJob
import rest_framework.status as status
from .serializers import ApplicantSignupSerializer, PostedJobSerializer, RecruiterSignupSerializer, UserLoginSerializer

class ApplicantSignupView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = ApplicantSignupSerializer
    permission_classes = [AllowAny]

class RecruiterSignupView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = RecruiterSignupSerializer
    permission_classes = [AllowAny]

class UserLoginView(generics.GenericAPIView):
    serializer_class = UserLoginSerializer
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        
        token, created = Token.objects.get_or_create(user=user)
        
        return Response({
            'token': token.key,
            'usertype': user.usertype
        }, status=status.HTTP_200_OK)


class PostedJobView(generics.ListCreateAPIView):
    queryset = PostedJob.objects.all()
    serializer_class = PostedJobSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)