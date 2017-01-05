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


class BlogArticlePage(Page):
    body = RichTextField()
    intro = models.CharField(max_length=250, default='')
    date = models.DateField("Post date")

    content_panels = Page.content_panels + [
        FieldPanel('date'),
        FieldPanel('intro'),
        FieldPanel('body', classname="full"),
    ]
