from django.contrib import admin
from django.urls import path, include
import os 

admin.site.site_header = 'Sparks of Africa Admin'
urlpatterns = [
    path(f"{os.environ.get('SECRET_ADMIN_PATH')}admin/", admin.site.urls),
    path('', include('website.urls')),
    path('appboard/', include('dashboard.urls')),
    path('accounts/', include('allauth.urls')),
]
