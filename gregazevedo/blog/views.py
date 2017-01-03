from django.shortcuts import render
from django.views.generic.base import TemplateView


class BlogHomeView(TemplateView):
    template_name = 'blog.html'
