from django.conf.urls import url

from floc.views import FlocTemplateView
from .views import PlayListView, PlayDetailView


urlpatterns = [
    url(r'^$', PlayListView.as_view(), name='play-list'),
    url(r'^(?P<slug>[-\w]+)/$', PlayDetailView.as_view(), name='play-detail'),
]
