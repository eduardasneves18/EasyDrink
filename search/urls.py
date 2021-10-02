from django.urls import path,include
from search.views import SearchProductView,SearchViewSet
from rest_framework import routers

app_name = 'search'

router = routers.DefaultRouter()
router.register('',SearchViewSet)

urlpatterns = [
    path('',SearchProductView.as_view(),name='query'),
    path('search/', include((router.urls))),
]