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
@register_streamfield_block
class _S_GitlabBlock(blocks.StructBlock):
    name = blocks.CharBlock(
        null=True, required=True, help_text="Name of the presentator"
    )
    url = blocks.URLBlock(
        null=True,
        required=True,
        help_text="Important! Format https://www.domain.tld/xyz",
    )
    description = blocks.TextBlock(
        null=True, required=False, help_text="Other information"
    )
    mode = blocks.ChoiceBlock(
        choices=[("polp", "Principle of least privilege"), ("idc", "Open privilege"),]
    )
    pat = blocks.CharBlock()


# > Pages
class OpsGitlabsPage(Page):
    # Only allow creating HomePages at the root level
    parent_page_types = ["ops_scpages.OpsScpagesPage"]

    gitlabs_section = fields.StreamField(
        [("_S_GitlabBlock", _S_GitlabBlock(null=True, icon="fa-gitlab")),],
        null=True,
        blank=False,
    )

    graphql_fields = [
        GraphQLStreamfield("gitlabs_section"),
    ]

    main_content_panels = [
        StreamFieldPanel("gitlabs_section"),
    ]

    content_panels = Page.content_panels + main_content_panels


# SPDX-License-Identifier: (EUPL-1.2)
# Copyright © 2019-2020 Simon Prast
