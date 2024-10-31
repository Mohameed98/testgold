# datasetapp/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('date_input/', views.date_input_view, name='date_input'),
]
