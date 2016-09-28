from django.shortcuts import render

from floc.views import FlocTemplateView


class ActorListView(FlocTemplateView):
    template_name = 'actors/actor_list.html'
