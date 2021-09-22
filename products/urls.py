from django.urls import path, include
from products.views import CategoryViewSet, ProductViewSet, get_products_by_category
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('categories', CategoryViewSet)
router.register('list', ProductViewSet)

#forma utilizada prara trazer items de uma categoria especifica 
urlpatterns = [
    path('products/category/<str:cat>', get_products_by_category, name="get_products_by_category"),
    path('', include(router.urls))
]