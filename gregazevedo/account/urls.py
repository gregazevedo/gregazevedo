from django.conf.urls import url, include
urlpatterns = []
from .views import login, RegistrationView # NOQA
from django.contrib.auth import urls as auth_urls

urlpatterns.extend([
    url(r'^login/$', login, name='login'),
    url(r'^member/register/$',
        RegistrationView.as_view(),
        name='register'),
    url(r'', include(auth_urls)),
])
