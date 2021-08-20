from .models import User
from .serializers import UserSerializer
from rest_framework import viewsets, permissions


class UserViewSet(viewsets.ModelViewSet):
  permission_classe = (permissions.IsAuthenticated,)
  queryset = User.objects.all()
  serializer_class = UserSerializer

  def get_queryset(self):
    categories = User.objects.all()
    return categories