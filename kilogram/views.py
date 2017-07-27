from django.views.generic.base import TemplateView

class IndexView(TemplateView): # TemplateView를 상속 받는다.
    template_name = 'kilogram/index.html'