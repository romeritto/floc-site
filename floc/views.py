from django.views.generic import TemplateView
from django.views.generic.base import ContextMixin

from blog.models import Blogpost


class FlocContextMixin(ContextMixin):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['recent_blogposts'] = Blogpost.objects.all()[:3]

        return context


class FlocTemplateView(FlocContextMixin, TemplateView):
    pass


class IndexView(FlocTemplateView):
    template_name = 'index.html'
