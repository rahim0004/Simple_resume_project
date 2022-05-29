from tkinter import N
from django.urls import path
from edu import views

urlpatterns = [
    path('',views.skill, name='skill' ),
]
