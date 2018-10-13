from django.urls import re_path

from .views import BlogpostListView, BlogpostDetailView

app_name='blog'
urlpatterns = [
    re_path(r'^$', BlogpostListView.as_view(), name='blogpost-list'),
    re_path(
        r'^(?P<slug>[-\w]+)/$',
        BlogpostDetailView.as_view(),
        name='blogpost-detail',
    ),
]
