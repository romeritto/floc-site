from django.views.generic import TemplateView
from django.views.generic.base import ContextMixin

from blog.models import Blogpost
from shows.models import Show
from actors.models import Quote


class FlocContextMixin(ContextMixin):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['recent_blogposts'] = Blogpost.objects.all()[:3]

        return context


class FlocTemplateView(FlocContextMixin, TemplateView):
    pass


class IndexView(FlocTemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['upcoming_shows_limit_3'] = Show.objects.upcoming().order_by(
                                                'start_time'
                                            )[:3]
        context['actor_quotes'] = Quote.objects.all()

        return context
