from django.db import models
from django.conf import settings
from wagtail.core.models import Page
from wagtail.core import fields
from wagtail.core import blocks
from wagtail.documents import blocks as docblocks
from wagtail.images.blocks import ImageChooserBlock
from wagtail.snippets.blocks import SnippetChooserBlock
from wagtail.embeds.blocks import EmbedBlock
from wagtail.admin.edit_handlers import (
    StreamFieldPanel,
    FieldPanel,
    PageChooserPanel,
    TabbedInterface,
    ObjectList,
    InlinePanel,
    MultiFieldPanel,
)
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.snippets.models import register_snippet

import uuid

from esite.bifrost.models import (
    GraphQLInt,
    GraphQLBoolean,
    GraphQLString,
    GraphQLFloat,
    GraphQLImage,
    GraphQLDocument,
    GraphQLSnippet,
    GraphQLEmbed,
    GraphQLStreamfield,
)
from esite.bifrost.helpers import register_streamfield_block

# > Sections


class Connector_SettingsBlock(blocks.StructBlock):
    # shared_projects =
    # shared_users =
    # shared_contributions =
    # shared_statistics =
    # shared_companydata =
    # mode =
    pass


@register_streamfield_block
class _S_ConnectorBlock(blocks.StructBlock):
    from ..ops_scpages.models import OpsScpagesPage

    name = blocks.CharBlock(
        null=True, required=True, help_text="Name of the presentator"
    )
    domain = blocks.URLBlock(
        null=True,
        required=True,
        help_text="Important! Format https://www.domain.tld/xyz",
    )
    """[Future implementation]
    
    There should be a chooser block containing ops_scpages pages. 
    """
    related_page = models.ForeignKey(
        "wagtailcore.Page",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
    )
    page = blocks.PageChooserBlock(required=False, target_model=OpsScpagesPage)

    mode = blocks.ChoiceBlock(
        choices=[
            (
                "isolate",
                "Prohibit external authentication - Prohibit company page publishing",
            ),
            (
                "medium",
                "Prohibit external authentication - Allow company page publishing",
            ),
            ("open", "Allow external authentication - Allow company page publishing"),
        ]
    )
    pat = blocks.CharBlock()


# > Pages
class OpsConnectorsPage(Page):
    # Only allow creating HomePages at the root level
    parent_page_types = ["wagtailcore.Page"]

    connector_section = fields.StreamField(
        [("_S_ConnectorBlock", _S_ConnectorBlock(null=True, icon="cogs")),],
        null=True,
        blank=True,
    )

    main_content_panels = [
        StreamFieldPanel("connector_section"),
    ]

    content_panels = Page.content_panels + main_content_panels


# SPDX-License-Identifier: (EUPL-1.2)
# Copyright © 2019-2020 Simon Prast
