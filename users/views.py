from rest_framework import generics
from rest_framework import permissions

from users.models import User
from users.serializers import UserSerializer, UserProfileSerializer


# Create your views here.


# Sign up the user
class UserCreateAPIView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserRetrieveAPIView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserProfileSerializer

    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user