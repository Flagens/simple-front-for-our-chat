# example/urls.py
from django.urls import path

from . import views


urlpatterns = [
    path('', views.czat, name='czat'),
    path('odpowiedz/', views.odpowiedz, name='odpowiedz'),
]





