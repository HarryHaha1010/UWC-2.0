from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("", include("src.urls")),
    path('admin/', admin.site.urls),
    path('users/', include('django.contrib.auth.urls')),
    path('', include('users.urls')),
    path('',include("API.urls"))
]
