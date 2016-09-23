from django.views.generic import TemplateView


class FlocTemplateView(TemplateView):
    pass


class IndexView(FlocTemplateView):
    template_name = 'index.html'
