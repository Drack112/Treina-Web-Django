from django.contrib import admin
from django.urls import path, include

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Django Rest Framework Test",
        default_version="v1",
        description="Uma aplicação desenvolvido para aprender Django Rest Framework com outras tecnologias.",
        contact=openapi.Contact(email="onepessoa3@gmail.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path("api/", include("api.urls")),
    # Autenticação
    path("o/", include("oauth2_provider.urls", namespace="oauth2_provider")),
    # Documentação
    path(
        "swagger/",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
    path("redoc/", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"),
    path("admin/", include("admin_honeypot.urls", namespace="admin_honeypot")),
    path("secret/", include(admin.site.urls)),
]
