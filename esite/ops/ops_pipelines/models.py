import json
from django.db import models
from django.conf import settings
from django.core.serializers.json import DjangoJSONEncoder
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
from modelcluster.fields import ParentalKey
from wagtail.admin.edit_handlers import (
    FieldPanel,
    FieldRowPanel,
    InlinePanel,
    MultiFieldPanel,
)

import uuid
from wagtail.admin.mail import send_mail
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
from wagtail.contrib.forms.models import (
    AbstractForm,
    AbstractFormField,
    AbstractEmailForm,
    AbstractFormField,
    AbstractFormSubmission,
)

# > Sections
@register_streamfield_block
class Pipeline_ActivityBlock(blocks.StructBlock):
    datetime = blocks.DateTimeBlock(null=True, required=True)


@register_streamfield_block
class _S_PipelineBlock(blocks.StructBlock):
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
    activity_history = blocks.StreamBlock(
        [
            (
                "activity",
                Pipeline_ActivityBlock(
                    null=True, blank=False, icon="fa-calendar-check-o"
                ),
            )
        ],
        null=True,
        blank=False,
    )
    verified = blocks.BooleanBlock(
        null=False,
        required=False,
        default=False,
        help_text="Whether the attendee was attending or not",
    )
    token = blocks.CharBlock()

    graphql_fields = [
        GraphQLString("name"),
        GraphQLString("url"),
        GraphQLString("description"),
        GraphQLString("activity_history"),
        GraphQLString("verified"),
    ]


# > Pages
class OpsPipelinesPage(Page):
    # Only allow creating HomePages at the root level
    # parent_page_types = ["wagtailcore.Page"]

    sections = fields.StreamField(
        [("S_PipelineBlock", _S_PipelineBlock(null=True, icon="cogs")),],
        null=True,
        blank=False,
    )

    graphql_fields = [
        GraphQLStreamfield("sections"),
    ]

    main_content_panels = [
        StreamFieldPanel("sections"),
    ]

    content_panels = Page.content_panels + main_content_panels

    preview_modes = []


# Form
class PipelineFormField(AbstractFormField):
    page = ParentalKey(
        "PipelineFormPage", on_delete=models.CASCADE, related_name="form_fields",
    )


class PipelineFormPage(AbstractEmailForm):
    # When creating a new Form page in Wagtail
    head = models.CharField(null=True, blank=False, max_length=255)
    description = models.CharField(null=True, blank=False, max_length=255)

    graphql_fields = [
        GraphQLString("head"),
        GraphQLString("description"),
    ]

    content_panels = AbstractEmailForm.content_panels + [
        MultiFieldPanel(
            [
                FieldPanel("head", classname="full title"),
                FieldPanel("description", classname="full"),
            ],
            heading="content",
        ),
        MultiFieldPanel(
            [
                FieldRowPanel(
                    [
                        FieldPanel("from_address", classname="col6"),
                        FieldPanel("to_address", classname="col6"),
                    ]
                ),
                FieldPanel("subject"),
            ],
            heading="Email Settings",
        ),
        MultiFieldPanel(
            [InlinePanel("form_fields", label="Form fields")], heading="data",
        ),
    ]

    def get_submission_class(self):
        return PipelineFormSubmission

    # Create a new user
    def create_or_update_pipeline(
        self, git, log, activity_data,
    ):
        # enter the data here

        parent_page = Page.objects.get(slug="pipelines").specific

        pipeline_page = OpsPipelinesPage(
            title=f"f",
            slug=f"ff",
            # section=[
            #     {
            #         "type": "S_PipelineBlock",
            #         "value": {
            #             "name": "Lookingglass",
            #             "url": "http://gitlab.local/anexia/lookingglass",
            #             "description": "A beautifully executed piece of art.",
            #             "activity_log": [
            #                 {
            #                     "type": "activity",
            #                     "value": {"datetime": "2020-08-12T03:00:00+02:00"},
            #                     "id": "1821fae3-c31d-41af-83ce-1a06de5778fa",
            #                 },
            #                 {
            #                     "type": "activity",
            #                     "value": {"datetime": "2020-08-13T04:00:00+02:00"},
            #                     "id": "3bc2609e-24b2-440a-ba39-93deffefef95",
            #                 },
            #                 {
            #                     "type": "activity",
            #                     "value": {"datetime": "2020-08-11T05:00:00+02:00"},
            #                     "id": "9c54354a-65a2-4cd8-8c42-0bdd94cfdf57",
            #                 },
            #             ],
            #             "verified": True,
            #             "token": "fc502377-0edb-4ce4-9488-d2e8aac7f578",
            #         },
            #         "id": "ed88f7ec-5550-49ae-b28a-d3fe4c2b38b4",
            #     }
            # ],
        )

        return pipeline_page

    # Called when pipeline data is pushed
    def send_mail(self, form):
        addresses = [x.strip() for x in self.to_address.split(",")]

        emailheader = "New SNEK OPS Pipeline"

        content = []
        for field in form:
            value = field.value()
            if isinstance(value, list):
                value = ", ".join(value)
            content.append("{}: {}".format(field.label, value))
        content = "\n".join(content)

        content += "\n\nMade with ❤ by a tiny SNEK"

        # emailfooter = '<style>@keyframes pulse { 10% { color: red; } }</style><p>Made with <span style="width: 20px; height: 1em; color:#dd0000; animation: pulse 1s infinite;">&#x2764;</span> by <a style="color: lightgrey" href="https://www.aichner-christian.com" target="_blank">Werbeagentur Christian Aichner</a></p>'

        # html_message = f"{emailheader}\n\n{content}\n\n{emailfooter}"

        send_mail(
            self.subject, f"{emailheader}\n\n{content}", addresses, self.from_address
        )

    def process_form_submission(self, form):

        pipelinepage = self.create_or_update_pipeline(
            git=form.cleaned_data["git"],
            log=form.cleaned_data["log"],
            activity_data=json.dumps(form.cleaned_data, cls=DjangoJSONEncoder),
        )

        self.get_submission_class().objects.create(
            form_data=json.dumps(form.cleaned_data, cls=DjangoJSONEncoder), page=self,
        )

        if self.to_address:
            self.send_mail(form)


class PipelineFormSubmission(AbstractFormSubmission):
    pass
    # user = models.ForeignKey(OpsPipelinesPage, on_delete=models.CASCADE)


# SPDX-License-Identifier: (EUPL-1.2)
# Copyright © 2019-2020 Simon Prast
