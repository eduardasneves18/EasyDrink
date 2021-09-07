from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.schemas import get_schema_view
from rest_framework.documentation import include_docs_urls

urlpatterns = [
    # Authentication
    # path('auth/', include('drf_social_oauth2.urls', namespace='drf')),
    path ('auth/', include ('users.urls')),

    # Admin
    path ('admin/', admin.site.urls),

    #Anothers endpoints
    path('api/v1/', include('products.urls')),
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