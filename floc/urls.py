"""floc URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""

from django.conf import settings
from django.conf.urls import url, include
from django.contrib import admin

from .views import FlocTemplateView, IndexView

urlpatterns = [
    url(r'^$', IndexView.as_view(), name='index'),
    url(r'^admin/', admin.site.urls),
    url(r'^program/', include('shows.urls', namespace='shows')),
    url(r'^blog/', include('blog.urls', namespace='blog')),
    url(r'^inscenacie/', include('plays.urls', namespace='plays')),
    url(r'^o-nas/herci/', include('actors.urls', namespace='actors')),
    url(
        r'^o-nas/historia/$',
        FlocTemplateView.as_view(template_name='history.html'),
        name='history'
    ),
    url(
        r'^kontakt/$',
        FlocTemplateView.as_view(template_name='contact.html'),
        name='contact'
    ),
    url(r'^tinymce/', include('tinymce.urls')),
]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
