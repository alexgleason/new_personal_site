from django.db import models

from wagtail.core import blocks

from wagtail.core.models import Page

from wagtail.core.fields import StreamField

from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel, MultiFieldPanel

from website.blocks import ImageInfoSection, PortalCard


class HomePage(Page):
    portal_cards = StreamField(
        [
            ('portal_card', PortalCard())
        ]
    )
    body = StreamField(
        [
            ('image_info_section', ImageInfoSection())
        ]
    )

    content_panels = Page.content_panels + [
        StreamFieldPanel('portal_cards'),
        StreamFieldPanel('body'),
    ]
