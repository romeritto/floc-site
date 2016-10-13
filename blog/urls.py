from django.conf.urls import url

from .views import BlogpostListView, BlogpostDetailView


urlpatterns = [
    url(r'^$', BlogpostListView.as_view(), name='blogpost-list'),
    url(
        r'^(?P<slug>[-\w]+)/$',
        BlogpostDetailView.as_view(),
        name='blogpost-detail',
    ),
]
