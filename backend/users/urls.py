from django.urls import path, include
from users.views import UserViewSet
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('users', UserViewSet)

app_name = 'users'
 
urlpatterns = [
    path('', include(router.urls))
]

