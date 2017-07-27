from django.shortcuts import render
from django.views.generic.base import TemplateView

class IndexView(TemplateView): # TemplateView를 상속 받는다.
    template_name = 'kilogram/index.html'


def post_list(request):
    return render(request, 'kilogram/post_list.html', {})
