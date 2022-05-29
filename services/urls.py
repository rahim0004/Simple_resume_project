from django.urls import path
from services import views

# app_name = 'services'

urlpatterns = [
    path('',views.services, name='service'),
]
