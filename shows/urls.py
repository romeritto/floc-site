from django.urls import re_path

from .views import ShowTemplateView

app_name='shows'
urlpatterns = [
    re_path(r'^$', ShowTemplateView.as_view(), name='show-list'),
]
