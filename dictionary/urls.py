# dictionary/urls.py
from django.conf.urls import url
from django.urls import path
from django.views.generic.base import RedirectView
from .views import indexView, firstTranslate, ajaxTranslate

urlpatterns = [
     path('', indexView, name='index'),
     path('translate', firstTranslate),
     path('get/ajax/translate', ajaxTranslate, name="translate_ajax"),
     url(r'^favicon.ico', RedirectView.as_view(url="images/favicon.ico"))
]
