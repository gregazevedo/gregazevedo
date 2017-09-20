from django.db import models
from wagtail.wagtailcore.models import Page
from wagtail.wagtailcore.fields import RichTextField
from wagtail.wagtailadmin.edit_handlers import FieldPanel, PageChooserPanel


class BlogHomePage(Page):
    body = RichTextField()
    related_page = models.ForeignKey(
        'wagtailcore.Page',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
    )

    content_panels = Page.content_panels + [
        FieldPanel('body', classname="full"),
        PageChooserPanel('related_page', 'blog.BlogArticlePage'),
    ]

    def get_context(self, request):
        context = super(BlogHomePage, self).get_context(request)
        pages = self.get_children().specific().live()
        context['articles'] = pages.order_by('-blogarticlepage__date')
        return context


class BlogArticlePage(Page):
    body = RichTextField()
    intro = models.CharField(max_length=250, default='')
    date = models.DateField("Post date")

    content_panels = Page.content_panels + [
        FieldPanel('date'),
        FieldPanel('intro'),
        FieldPanel('body', classname="full"),
    ]
