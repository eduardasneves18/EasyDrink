   
from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register('', views.CartViewSet)
router.register('delivery-cost', views.DeliveryCostViewSet)

urlpatterns = [
    path('', include((router.urls, 'shopping_cart_api.cart'))),
]