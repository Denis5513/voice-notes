from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from . import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("core/", include("core.urls", namespace="core")),
    path("", views.home, name='home'),
    path('authorization_message', views.authorization_required, name='authorization_message'),
    path('users/', include('users.urls')),
    path('notes/', include('notes.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)