from django.views.generic import TemplateView
from django.views.generic.base import ContextMixin


class FlocContextMixin(ContextMixin):
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['test'] = 'easy'
        return context


class FlocTemplateView(FlocContextMixin, TemplateView):
    pass


class IndexView(FlocTemplateView):
    template_name = 'index.html'
