from django.urls import re_path

from .views import ActorListView

app_name='actors'
urlpatterns = [
    re_path(r'^$', ActorListView.as_view(), name='actor-list'),
]
