from django.conf.urls import url

from .views import ActorListView


urlpatterns = [
    url(r'^$', ActorListView.as_view(), name='actor-list'),
]
