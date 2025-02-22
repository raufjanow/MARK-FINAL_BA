from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('portfolio-details/', views.portfolio_details, name='portfolio-details'),
    path('service-details/', views.service_details, name='service-details'),
    path('starter-page/', views.starter_page, name='starter-page'),
    path('contact/', views.contact, name='contact'),
]