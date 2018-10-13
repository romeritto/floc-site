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
from django.urls import include, re_path
from django.contrib import admin

from .views import FlocTemplateView, IndexView, contact_form_submit

urlpatterns = [
    re_path(r'^$', IndexView.as_view(), name='index'),
    re_path(r'^admin/', admin.site.urls),
    re_path(r'^program/', include('shows.urls')),
    re_path(r'^blog/', include('blog.urls')),
    re_path(r'^inscenacie/', include('plays.urls')),
    re_path(r'^o-nas/herci/', include('actors.urls')),
    re_path(
        r'^o-nas/historia/$',
        FlocTemplateView.as_view(template_name='history.html'),
        name='history'
    ),
    re_path(
        r'^kontakt/$',
        FlocTemplateView.as_view(template_name='contact.html'),
        name='contact'
    ),
    re_path(
        r'^kontakt/form-submit/$',
        contact_form_submit,
        name='contact-form-submit'
    ),
]

if settings.DEBUG:
    import debug_toolbar
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += [
        re_path(r'^__debug__/', include(debug_toolbar.urls)),
    ]
