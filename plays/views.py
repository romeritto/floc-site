from django.views.generic import ListView, DetailView

from floc.views import FlocContextMixin
from .models import Play


class PlayListView(FlocContextMixin, ListView):
    model = Play
    context_object_name = 'play_objects'

    def get_context_data(self, **kwargs):
        def get_distinct_years():
            dates = Play.objects.values('premiere_date')
            distinct_years = list(set([d['premiere_date'].year for d in dates]))
            return sorted(distinct_years, reverse=True)

        context = super().get_context_data(**kwargs)

        context['play_years'] = get_distinct_years()

        return context


class PlayDetailView(FlocContextMixin, DetailView):
    model = Play
    context_object_name = 'play'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['other_plays'] = Play.objects.exclude(pk=self.object.id)[:4]

        return context
