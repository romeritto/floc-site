from django.views.generic import TemplateView


class FlocTemplateView(TemplateView):
    pass


class IndexView(FlocTemplateView):
    template_name = 'index.html'


class HistoryView(FlocTemplateView):
    template_name = 'history.html'


class ContactView(FlocTemplateView):
    template_name = 'contact.html'
