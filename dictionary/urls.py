# dictionary/urls.py
from django.urls import path

from . import views


urlpatterns = [
     path('', views.show_index, name='index'),
     path('translate/', views.translate),
]