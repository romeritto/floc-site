from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^$', views.ActorListView.as_view(), name='actor_list'),
]
