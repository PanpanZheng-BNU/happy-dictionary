# dictionary/urls.py
from django.urls import path

from .views import indexView, firstTranslate, ajaxTranslate


urlpatterns = [
     path('', indexView, name='index'),
     path('translate', firstTranslate),
     path('get/ajax/translate', ajaxTranslate, name="translate_ajax"),
]
