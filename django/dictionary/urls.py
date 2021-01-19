# dictionary/urls.py
from django.urls import path
from . import views


urlpatterns = [
     path('', views.show_index, name='index'),
     path(r'translate/', views.translate),
]
