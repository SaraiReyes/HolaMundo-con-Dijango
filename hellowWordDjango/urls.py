from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('centro/', include('centro.urls')),
    path('admin/', admin.site.urls),
]