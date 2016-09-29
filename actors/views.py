from django.views.generic import ListView

from floc.views import FlocContextMixin
from .models import Actor


class ActorListView(FlocContextMixin, ListView):
    model = Actor
    context_object_name = 'actor_objects'
