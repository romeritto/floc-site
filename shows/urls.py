from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^$', views.ShowsView.as_view(), name='shows'),
]
