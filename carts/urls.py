   
from django.urls import include, path
from rest_framework import routers
from . import views
from .views import checkout

router = routers.DefaultRouter()
router.register('', views.CartViewSet)
router.register('delivery-cost', views.DeliveryCostViewSet)

urlpatterns = [
    path('checkout',checkout, name="checkout"),
    path('', include((router.urls, 'shopping_cart_api.cart'))),
]