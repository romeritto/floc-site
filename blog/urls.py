from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^$', views.BlogpostListView.as_view(), name='blogpost_list'),
]
