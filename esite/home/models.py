from django.db import models

from wagtail.core.models import Page
from wagtail.core import fields
from wagtail.core import blocks
from wagtail.documents import blocks as docblocks
from wagtail.images import blocks as imgblocks
from wagtail.snippets import blocks as snipblocks
from wagtail.embeds import blocks as embedsblocks
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.snippets.edit_handlers import SnippetChooserPanel
from wagtail.admin.edit_handlers import (
    StreamFieldPanel,
    FieldPanel,
    PageChooserPanel,
    TabbedInterface,
    ObjectList,
    InlinePanel,
    MultiFieldPanel,
)
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
    GraphQLForeignKey,
    GraphQLPage,
)
from esite.bifrost.helpers import register_streamfield_block

# > Sections
@register_streamfield_block
class _S_SmallBlock(blocks.StructBlock):
    charblock = blocks.CharBlock()
    textblock = blocks.TextBlock()
    emailblock = blocks.EmailBlock()

    graphql_fields = [
        GraphQLString("charblock"),
        GraphQLString("textblock"),
        GraphQLString("emailblock"),
    ]


@register_streamfield_block
class _S_BigBlock(blocks.StructBlock):
    integerblock = blocks.IntegerBlock()
    floatblock = blocks.FloatBlock()
    decimalblock = blocks.DecimalBlock()
    regexblock = blocks.RegexBlock(regex="")
    urlblock = blocks.URLBlock()
    booleanblock = blocks.BooleanBlock()
    dateblock = blocks.DateBlock()

    graphql_fields = [
        GraphQLInt("integerblock"),
        GraphQLFloat("floatblock"),
        GraphQLFloat("decimalblock"),
        GraphQLString("regexblock"),
        GraphQLString("urlblock"),
        GraphQLBoolean("booleanblock"),
        GraphQLString("dateblock"),
    ]


@register_streamfield_block
class _S_TallBlock(blocks.StructBlock):
    timeblock = blocks.TimeBlock()
    datetimeblock = blocks.DateTimeBlock()
    richtextblock = blocks.RichTextBlock()
    rawhtmlblock = blocks.RawHTMLBlock()
    blockquoteblock = blocks.BlockQuoteBlock()
    choiceblock = blocks.ChoiceBlock(
        choices=[("apples", "Apple"), ("bananas", "Bananas"),]
    )
    # pagechooserblock = blocks.PageChooserBlock()

    graphql_fields = [
        GraphQLString("timeblock"),
        GraphQLString("datetimeblock"),
        GraphQLString("richtextblock"),
        GraphQLString("rawhtmlblock"),
        GraphQLString("blockquoteblock"),
        GraphQLString("choiceblock"),
        # GraphQLForeignKey("pagechooserblock", content_type="page"),
    ]


@register_streamfield_block
class _S_LightBlock(blocks.StructBlock):
    documentchooserblock = docblocks.DocumentChooserBlock()
    imagechooserblock = imgblocks.ImageChooserBlock()
    snippetchooserblock = snipblocks.SnippetChooserBlock(target_model="utils.Button")
    embedblock = embedsblocks.EmbedBlock()
    staticblock = blocks.StaticBlock()

    graphql_fields = [
        GraphQLDocument("documentchooserblock"),
        GraphQLImage("imagechooserblock"),
        GraphQLSnippet("snippetchooserblock", snippet_model="utils.Button"),
        GraphQLEmbed("embedblock"),
        GraphQLString("staticblock"),
    ]


# > Pages
class HomePage(Page):
    template = "patterns/pages/home/home_page.html"

    # Only allow creating HomePages at the root level
    parent_page_types = ["wagtailcore.Page"]
    # subpage_types = ['news.NewsIndex', 'standardpages.StandardPage', 'articles.ArticleIndex',
    #                 'people.PersonIndex', 'events.EventIndex']

    # autofield = models.AutoField()
    # bigautofield = models.BigAutoField()
    bigintegerfield = models.BigIntegerField(blank=False, null=True)
    # binaryfield = models.BinaryField()
    booleanfield = models.BooleanField(blank=False, null=True)
    charfield = models.CharField(max_length=22, blank=False, null=True)
    datefield = models.DateField(blank=False, null=True)
    datetimefield = models.DateTimeField(blank=False, null=True)
    decimalfield = models.DecimalField(
        decimal_places=5, max_digits=22, blank=False, null=True
    )
    durationfield = models.DurationField(blank=False, null=True)
    emailfield = models.EmailField(blank=False, null=True)
    filefield = models.FileField(blank=False, null=True)
    # filepathfield = models.FilePathField(blank=False, null=True)
    floatfield = models.FloatField(blank=False, null=True)
    imagefield = models.ImageField(blank=False, null=True)
    integerfield = models.IntegerField(blank=False, null=True)
    genericipaddressfield = models.GenericIPAddressField(blank=False, null=True)
    nullbooleanfield = models.NullBooleanField(blank=False, null=True)
    positiveintegerfield = models.PositiveIntegerField(blank=False, null=True)
    positivesmallintegerfield = models.SmallIntegerField(blank=False, null=True)
    slugfield = models.SlugField(blank=False, null=True)
    smallintegerfield = models.SmallIntegerField(blank=False, null=True)
    textfield = models.TextField(blank=False, null=True)
    timefield = models.TimeField(blank=False, null=True)
    urlfield = models.URLField(blank=False, null=True)
    uuidfield = models.UUIDField(blank=False, null=True, default=uuid.uuid4)

    sections = fields.StreamField(
        [
            ("s_smallblock", _S_SmallBlock()),
            ("s_bigblock", _S_BigBlock()),
            ("s_tallblock", _S_TallBlock()),
            ("s_lightblock", _S_LightBlock()),
        ],
        null=True,
        blank=False,
    )

    graphql_fields = [
        # GraphQLInt("autofield"),
        # GraphQLInt("bigautofield"),
        GraphQLInt("bigintegerfield"),
        GraphQLInt("binaryfield"),
        GraphQLBoolean("booleanfield"),
        GraphQLString("charfield"),
        GraphQLString("datefield"),
        GraphQLString("datetimefield"),
        GraphQLFloat("decimalfield"),
        GraphQLString("durationfield"),
        GraphQLString("emailfield"),
        # GraphQLGenericScala("filefield"),
        GraphQLString("filepathfield"),
        GraphQLFloat("floatfield"),
        # GraphQLGenericScala("imagefield"),
        GraphQLInt("integerfield"),
        GraphQLString("genericipaddressfield"),
        GraphQLBoolean("nullbooleanfield"),
        GraphQLInt("positiveintegerfield"),
        GraphQLString("slugfield"),
        GraphQLInt("smallintegerfield"),
        GraphQLString("textfield"),
        GraphQLString("timefield"),
        GraphQLString("urlfield"),
        GraphQLString("uuidfield"),
        GraphQLStreamfield("sections"),
        GraphQLInt("positivesmallintegerfield"),
    ]

    main_content_panels = [
        FieldPanel("bigintegerfield"),
        FieldPanel("booleanfield"),
        FieldPanel("charfield"),
        FieldPanel("datefield"),
        FieldPanel("datetimefield"),
        FieldPanel("decimalfield"),
        FieldPanel("durationfield"),
        FieldPanel("emailfield"),
        FieldPanel("filefield"),
        # FieldPanel('filepathfield'),
        FieldPanel("floatfield"),
        ImageChooserPanel("imagefield"),
        FieldPanel("integerfield"),
        FieldPanel("genericipaddressfield"),
        FieldPanel("nullbooleanfield"),
        FieldPanel("positiveintegerfield"),
        FieldPanel("positivesmallintegerfield"),
        FieldPanel("slugfield"),
        FieldPanel("smallintegerfield"),
        FieldPanel("textfield"),
        FieldPanel("timefield"),
        FieldPanel("urlfield"),
        FieldPanel("uuidfield"),
        StreamFieldPanel("sections"),
    ]

    content_panels = Page.content_panels + main_content_panels


# SPDX-License-Identifier: (EUPL-1.2)
# Copyright © 2019 Werbeagentur Christian Aichner
