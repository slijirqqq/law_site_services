from django.urls import path

from . import views

urlpatterns = [
    path('', views.home_page_view, name='home'),
    path('about/', views.AboutListView.as_view(), name='about'),
    path('services/', views.ServicesListView.as_view(), name='services'),
    path('service/<int:pk>/', views.ServiceDetail.as_view(), name='service-detail'),
    path('contact/', views.ContactView.as_view(), name='contact')
]
