from django.conf.urls import url, include
from .views import BlogHomeView
urlpatterns = []

urlpatterns.extend([
    url(r'^$', BlogHomeView.as_view(), name='blog'),
])
