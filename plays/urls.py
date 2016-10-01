from django.conf.urls import url

from .views import PlayListView


urlpatterns = [
    url(r'^$', PlayListView.as_view(), name='play_list'),
]
