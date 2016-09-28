from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^$', views.PlayListView.as_view(), name='play_list'),
]
