from urllib.parse import quote
from django.core import serializers
from django.shortcuts import render

from .forms import TranslationForm, TranslationForm2
from django.http import JsonResponse
from .iciba import iciba


def indexView(request):
    if request.method == 'POST':
        # 接受request.POST参数构造form类的实例
        form = TranslationForm(request.POST)
    else:
        form = TranslationForm()

    logo = 'static/images/logo2.jpg'
    return render(request, 'translate/index.html', {'form': form, 'logo': logo})

def firstTranslate(request):
    form = TranslationForm2()
    request.encoding = 'utf-8'
    if 'q' in request.GET and request.GET['q']:
        getText = "\"{}\"".format(request.GET['q'])
        jsResponse = iciba(quote(request.GET['q'], 'utf-8'))
    return render(request, 'translate/result.html', {'form': form, 'forjson': jsResponse, 'getText2': getText})


def ajaxTranslate(request):
    if request.is_ajax and request.method == "GET":
        translateText = request.GET.get("translateText", None)
        jsResponse2 = iciba(quote(translateText, 'utf-8'))

        return JsonResponse({'forjson': jsResponse2}, status=200)

