from django.views.generic import ListView, DetailView

from floc.views import FlocContextMixin
from blog.models import Blogpost
from .models import Play, PlayCharacter


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

        context.update({
            'characters': PlayCharacter.objects.select_related(
                            'actor',
                            'actor__user',
                        ).filter(play=self.object),
            'other_plays': Play.objects.select_related(
                            'director',
                            'director__user',
                        ).exclude(pk=self.object.id)[:4],
            'related_blogposts': self.object.blogposts.all(),
        })

        return context
