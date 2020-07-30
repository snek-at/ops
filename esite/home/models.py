from django.db import models
from django.conf import settings
from wagtail.core.models import Page
from wagtail.core import fields
from wagtail.core import blocks
from wagtail.documents import blocks as docblocks
from wagtail.images.blocks import ImageChooserBlock
from wagtail.snippets.blocks import SnippetChooserBlock
from wagtail.embeds.blocks import EmbedBlock
from wagtail.admin.edit_handlers import StreamFieldPanel, FieldPanel, PageChooserPanel, TabbedInterface, ObjectList, InlinePanel, MultiFieldPanel
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.snippets.models import register_snippet

import uuid

#> Sections
class _S_SmallBlock(blocks.StructBlock):
    charblock = blocks.CharBlock()
    textblock = blocks.TextBlock()
    emailblock = blocks.EmailBlock()


class _S_BigBlock(blocks.StructBlock):
    integerblock = blocks.IntegerBlock()
    floatblock = blocks.FloatBlock()
    decimalblock = blocks.DecimalBlock()
    regexblock = blocks.RegexBlock(regex='')
    urlblock = blocks.URLBlock()
    booleanblock = blocks.BooleanBlock()
    dateblock = blocks.DateBlock()

class _S_TallBlock(blocks.StructBlock):
    timeblock = blocks.TimeBlock()
    datetimeblock = blocks.DateTimeBlock()
    richtextblock = blocks.RichTextBlock()
    rawhtmlblock = blocks.RawHTMLBlock()
    blockquoteblock = blocks.BlockQuoteBlock()
    choiceblock = blocks.ChoiceBlock(choices=[
        ('apples', 'Apple'),
        ('bananas', 'Bananas'),
    ])
    #pagechooserblock = blocks.PageChooserBlock()

class _S_LightBlock(blocks.StructBlock):
    documentchooserblock = docblocks.DocumentChooserBlock()
    imagechooserblock = ImageChooserBlock()
    snippetchooserblock = SnippetChooserBlock(target_model='utils.Button')
    embedblock = EmbedBlock()
    staticblock = blocks.StaticBlock()

#> Pages
class HomePage(Page):
    # Only allow creating HomePages at the root level
    parent_page_types = ['wagtailcore.Page']

    #autofield = models.AutoField()
    #bigautofield = models.BigAutoField()
    bigintegerfield = models.BigIntegerField(blank=False, null=True)
    #binaryfield = models.BinaryField()
    booleanfield = models.BooleanField(blank=False, null=True)
    charfield = models.CharField(max_length=22,blank=False, null=True)
    datefield = models.DateField(blank=False, null=True)
    datetimefield = models.DateTimeField(blank=False, null=True)
    decimalfield = models.DecimalField(decimal_places=5, max_digits=22,blank=False, null=True)
    durationfield = models.DurationField(blank=False, null=True)
    emailfield = models.EmailField(blank=False, null=True)
    #filefield = models.FileField(blank=False, null=True)
    #filepathfield = models.FilePathField(blank=False, null=True)
    floatfield = models.FloatField(blank=False, null=True)
    imagefield = models.ForeignKey(
        settings.WAGTAILIMAGES_IMAGE_MODEL,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
    )
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

    sections = fields.StreamField([
        ('s_smallblock', _S_SmallBlock()),
        ('s_bigblock', _S_BigBlock()),
        ('s_tallblock', _S_TallBlock()),
        ('s_lightblock', _S_LightBlock()),
    ], null=True, blank=False)

    main_content_panels = [
        FieldPanel('bigintegerfield'),
        FieldPanel('booleanfield'),
        FieldPanel('charfield'),
        FieldPanel('datefield'),
        FieldPanel('datetimefield'),
        FieldPanel('decimalfield'),
        FieldPanel('durationfield'),
        FieldPanel('emailfield'),
        #FieldPanel('filefield'),
        #FieldPanel('filepathfield'),
        FieldPanel('floatfield'),
        ImageChooserPanel('imagefield'),
        FieldPanel('integerfield'),
        FieldPanel('genericipaddressfield'),
        FieldPanel('nullbooleanfield'),
        FieldPanel('positiveintegerfield'),
        FieldPanel('positivesmallintegerfield'),
        FieldPanel('slugfield'),
        FieldPanel('smallintegerfield'),
        FieldPanel('textfield'),
        FieldPanel('timefield'),
        FieldPanel('urlfield'),
        FieldPanel('uuidfield'),
        StreamFieldPanel('sections'),
    ]

    content_panels = Page.content_panels + main_content_panels
