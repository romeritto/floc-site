from django.conf.urls import url

from .views import ShowTemplateView


urlpatterns = [
    url(r'^$', ShowTemplateView.as_view(), name='show-list'),
]
