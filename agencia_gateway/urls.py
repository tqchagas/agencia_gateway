from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('clientes/', include('clientes.urls')),
    path('hoteis/', include('hoteis.urls')),
    path('voos/', include('voos.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
