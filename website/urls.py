from django.urls import path
from . import views


urlpatterns = [
    path('', views.website_home, name='website_home'),
    path('blog', views.blog, name='blog'),
    path('causes', views.causes, name='causes'),
    path('contact', views.contact, name='contact'),
    path('donate', views.donate, name='donate'),
    path('event', views.event, name='event'),
    path('about/', views.about, name='about'),
    path('volunteer', views.volunteer, name='volunteer'),
    
]
