from django.conf.urls import url

from .views import BlogpostListView


urlpatterns = [
    url(r'^$', BlogpostListView.as_view(), name='blogpost-list'),
]
