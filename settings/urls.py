from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions
from sms.views import SmsView

schema_view = get_schema_view(
    openapi.Info(
        title="PITAK24 API DOCUMENTATION",
        description="REST API",
        default_version="1.0.0",
        terms_of_service="https://t.me/pitak24_bot",
        contact = openapi.Contact(email="farruxbekinfo@gmail.com"),
        license=openapi.License(name="Private"),
    ),
    public=False,
    permission_classes=(permissions.IsAdminUser,),
)

urlpatterns = [
    path('pitak-api-admin-farruxnet/', admin.site.urls),
    path('api/v1/', include('sms.urls')),
    path('api/v1/', include('users.urls')),
    path('docs-api-swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('docs-api-redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
