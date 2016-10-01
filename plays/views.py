from django.views.generic import ListView

from floc.views import FlocContextMixin
from .models import Play


class PlayListView(FlocContextMixin, ListView):
    model = Play
    context_object_name = 'play_objects'
