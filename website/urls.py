from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.website_home, name='website_home'),
    path('blog', views.blog, name='blog'),
    path('causes', views.causes, name='causes'),
    path('event_details/<str:pk>/', views.event_details, name='event_details'),
    path('cause_details/<str:pk>/', views.cause_details, name='cause_details'),
    path('contact', views.contact, name='contact'),
    path('donate', views.donate, name='donate'),
    path('event', views.events, name='event'),
    path('about/', views.about, name='about'),
    path('volunteer', views.volunteer, name='volunteer'),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
