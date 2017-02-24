from .views import error, ExampleFormView, AboutView

from django.conf.urls import url

from django.views.generic.base import TemplateView, RedirectView


urlpatterns = [
    url(r'^error/', error, name='error'),
    url(r'^$', TemplateView.as_view(template_name="index.html"), name="home"),
    url(r'^form/', ExampleFormView.as_view(), name="Example Form"),
    url(r'about/', AboutView.as_view(), name='about'),
    url(r'^facebook/', RedirectView.as_view(url='http://www.facebook.com/azevedo'), name='facebook'),
    url(r'^flickr/', RedirectView.as_view(url='http://www.flickr.com/photos/gregunit123/'), name='flickr'),
    url(r'^/foursquare', RedirectView.as_view(url='https://foursquare.com/gregazevedo'), name='foursquare'),
    url(r'^/github', RedirectView.as_view(url='https://github.com/gregazevedo'), name='github'),
    url(r'^/google', RedirectView.as_view(url='https://plus.google.com/u/0/106606482700752864288/posts'), name='google'),
    url(r'^/instagram', RedirectView.as_view(url='http://instagram.com/gregazevedo'), name='instagram'),
    url(r'^/linkedin', RedirectView.as_view(url='http://www.linkedin.com/pub/gregory-azevedo/4a/105/39'), name='linkedin'),
    url(r'^/stackoverflow', RedirectView.as_view(url='http://stackoverflow.com/users/3079110/greg'), name='stackoverflow'),
    url(r'^/tumblr', RedirectView.as_view(url='http://gregsreblogs.tumblr.com'), name='tumblr'),
    url(r'^/twitter', RedirectView.as_view(url='https://twitter.com/GregAzevedo'), name='twitter'),
    url(r'^/youtube', RedirectView.as_view(url='https://www.youtube.com/channel/UCoO-hFuDD3vAdVHGtSf0Jaw/feed'), name='youtube'),
]
