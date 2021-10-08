from django.urls import path, include
from products.views import CategoryViewSet, ProductViewSet, get_products_by_category, get_products_search
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('categories', CategoryViewSet)
router.register('', ProductViewSet)

#forma utilizada prara trazer items de uma categoria especifica 
urlpatterns = [
    path('category/<str:cat>', get_products_by_category, name="get_products_by_category"),
    path('search/<str:query>', get_products_search, name="get_products_search"),
    path('', include(router.urls))
]