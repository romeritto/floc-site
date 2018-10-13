from django.urls import re_path

from floc.views import FlocTemplateView
from .views import PlayListView, PlayDetailView

app_name='plays'
urlpatterns = [
    re_path(r'^$', PlayListView.as_view(), name='play-list'),
    re_path(r'^(?P<slug>[-\w]+)/$', PlayDetailView.as_view(), name='play-detail'),
]
