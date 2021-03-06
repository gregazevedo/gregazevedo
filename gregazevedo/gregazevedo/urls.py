from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin

from django.views.generic.base import RedirectView as rv
from django.views.static import serve as static_serve

from wagtail.wagtailadmin import urls as wagtailadmin_urls
from wagtail.wagtaildocs import urls as wagtaildocs_urls
from wagtail.wagtailcore import urls as wagtail_urls


urlpatterns = [
    url(r'^favicon\.ico$', rv.as_view(url='/static/img/favicon.ico', permanent=True)),
    url(r'account/', include('gregazevedo.account.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^blog/', include(wagtail_urls)),
    url('', include('social.apps.django_app.urls', namespace='social')),
    url(r'', include('gregazevedo.home.urls')),
    url(r'^cms/', include(wagtailadmin_urls)),
    url(r'^documents/', include(wagtaildocs_urls)),
]


if settings.DEBUG:
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns
    import debug_toolbar

    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += [
        url(r'^media/(?P<path>.*)$', static_serve, {
            'document_root': settings.MEDIA_ROOT,
        }),
        url(r'^__debug__/', include(debug_toolbar.urls)),
   ] # noqa
