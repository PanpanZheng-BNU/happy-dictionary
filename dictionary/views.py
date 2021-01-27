from django.shortcuts import render

from .forms import TranslationForm
from django.http import JsonResponse
from .iciba import iciba
from .get_picture import getBaidu

def indexView(request):
    if request.method == 'POST':
        # 接受request.POST参数构造form类的实例
        form = TranslationForm(request.POST)
    else:
        form = TranslationForm()

    logo = 'static/images/logo.svg'
    return render(request, 'translate/index.html', {'form': form, 'logo': logo})


def firstTranslate(request):
    form = TranslationForm()
    request.encoding = 'utf-8'

    return render(request, 'translate/result.html', {'form': form})


def ajaxTranslate(request):
    if request.is_ajax and request.method == "GET":
        translateText = request.GET.get("translateText", None)
        jsResponse2 = iciba(translateText)
        picUrl = getBaidu(translateText)

        return JsonResponse({'forjson': jsResponse2, 'picUrl': picUrl}, status=200)
