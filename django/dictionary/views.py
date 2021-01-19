import os
from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.conf import settings
from django.urls import reverse

from .forms import TranslationForm
from urllib.parse import quote
from .iciba import iciba


def show_index(request):
    if request.method == 'POST':
        # 接受request.POST参数构造form类的实例
        form = TranslationForm(request.POST)
    else:
        form = TranslationForm()

    logo = 'static/images/logo2.jpg'
    return render(request, 'translate/index.html', {'form': form, 'logo': logo})


def translate(request):
    request.encoding = 'utf-8'
    if 'q' in request.GET and request.GET['q']:
        message = iciba(quote(request.GET['q'], 'utf-8'))

    message2 = []

    for acceptationlist, poslist in zip(message.getElementsByTagName('acceptation'),
                                        message.getElementsByTagName('pos')):
        for acceptation, pos in zip(acceptationlist.childNodes, poslist.childNodes):
            message2.append(pos.data + acceptation.data)

    return render(request, 'translate/result.html', {'acceptation': message2})
