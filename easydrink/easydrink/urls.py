"""easydrink URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django import urls
from django.contrib import admin
from django.urls import path, include
from django.conf import settings 
from django.conf.urls.static import static
from rest_framework.schemas import get_schema_view
# from rest_framework.documentation import include_docs_urls
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
   openapi.Info(
      title="Easy Drink",
      default_version='v1',
      description="Easy drink application",
    #   terms_of_service="https://www.google.com/policies/terms/",
    #   contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    # Documentation
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    # Authentication
    # path('auth/', include('drf_social_oauth2.urls', namespace='drf')),
    path ('auth/', include ('users.urls')),

    # Admin
    path ('admin/', admin.site.urls),
    #Anothers endpoints
    path('api/v1/search', include('search.urls')),
    path('api/v1/products', include('products.urls')),
    # path('api/v1/', include('users.urls')),

    # API schema and Documentation
    # path('project/docs/', include_docs_urls(title='BlogAPI')),
    # path('project/schema', get_schema_view(
    #     title="BlogAPI",
    #     description="API for the BlogAPI",
    #     version="1.0.0"
    # ), name='openapi-schema'),
] 
# + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
