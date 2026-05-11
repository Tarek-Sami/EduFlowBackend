from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.views import TokenObtainPairView

from .models import User
from .serializers import (
    RegisterSerializer,
    EmailTokenObtainPairSerializer,
    CurrentUserSerializer,
)


class RegisterView(generics.CreateAPIView):
    serializer_class = RegisterSerializer


class EmailTokenObtainPairView(TokenObtainPairView):
    serializer_class = EmailTokenObtainPairSerializer


class CurrentUserView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        serializer = CurrentUserSerializer(request.user)
        return Response(serializer.data)


# GET /api/users/
# Returns all users in the accounts table.
# Currently accessible to any authenticated user.
# (You can later restrict this to admins only.)
class UserListView(generics.ListAPIView):
    queryset = User.objects.all().order_by("id")
    serializer_class = CurrentUserSerializer
    permission_classes = [IsAuthenticated]