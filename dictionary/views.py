import os

from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.conf import settings

from .forms import TaskForm

def get_name(request):
    # 如果form通过POST方法发送数据
    if request.method == 'POST':
        # 接受request.POST参数构造form类的实例
        form = TaskForm(request.POST)
    else:
        form = TaskForm()

    logo = 'static/images/logo2.jpg'

    return render(request, 'search/search.html', {'form': form, 'logo': logo})
# Create your views here.
