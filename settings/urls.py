from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions
from sms.views import SmsView
from rest_framework.documentation import include_docs_urls

schema_view = get_schema_view(
    openapi.Info(
        title="PITAK24 API DOCUMENTATION",
        description="REST API",
        default_version="VERSION 1",
        terms_of_service="https://google.com/poli",
        contact = openapi.Contact(email="farruxbekinfo@gmail.com"),
        license=openapi.License(name="Public"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('sms.urls')),
    path('api/v1/', include('users.urls')),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('docs/', include_docs_urls(title='Snippet API')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
