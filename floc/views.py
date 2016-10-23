import datetime

from django.http import JsonResponse
from django.views.generic import TemplateView
from django.views.generic.base import ContextMixin
from django.conf import settings

from blog.models import Blogpost
from shows.models import Show
from actors.models import Actor, Quote
from plays.models import Play


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

        def get_counters():

            # 3 hours of work per week
            # hours_of_work = (
            #    ((datetime.datetime.now() - settings.ESTABLISHMENT_DATE).days // 7) * 3
            # )

            counters = {
                'actors': Actor.objects.all().count(),
                'shows': Show.objects.all().count(),
                'plays': Play.objects.all().count(),
            }

            return counters

        context = super().get_context_data(**kwargs)

        context['upcoming_shows_limit_3'] = Show.objects.upcoming().order_by(
                                                'start_time'
                                            )[:3]
        context['actor_quotes'] = Quote.objects.all()
        context['counters'] = get_counters()

        return context


def contact_form_submit(request):

    if request.method == 'POST':
        return JsonResponse(
            {'response': 'success'}
        )
    else:
        return JsonResponse(
            {'response': 'error'}
        )
