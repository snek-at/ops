# Generated by Django 2.2.12 on 2020-07-31 22:49

from django.db import migrations, models
import django.db.models.deletion
import uuid
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.documents.blocks
import wagtail.embeds.blocks
import wagtail.images.blocks
import wagtail.snippets.blocks


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('wagtailcore', '0045_assign_unlock_grouppagepermission'),
        ('images', '0002_auto_20200729_2232'),
    ]

    operations = [
        migrations.CreateModel(
            name='OpsConnectorsPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('bigintegerfield', models.BigIntegerField(null=True)),
                ('booleanfield', models.BooleanField(null=True)),
                ('charfield', models.CharField(max_length=22, null=True)),
                ('datefield', models.DateField(null=True)),
                ('datetimefield', models.DateTimeField(null=True)),
                ('decimalfield', models.DecimalField(decimal_places=5, max_digits=22, null=True)),
                ('durationfield', models.DurationField(null=True)),
                ('emailfield', models.EmailField(max_length=254, null=True)),
                ('floatfield', models.FloatField(null=True)),
                ('integerfield', models.IntegerField(null=True)),
                ('genericipaddressfield', models.GenericIPAddressField(null=True)),
                ('nullbooleanfield', models.NullBooleanField()),
                ('positiveintegerfield', models.PositiveIntegerField(null=True)),
                ('positivesmallintegerfield', models.SmallIntegerField(null=True)),
                ('slugfield', models.SlugField(null=True)),
                ('smallintegerfield', models.SmallIntegerField(null=True)),
                ('textfield', models.TextField(null=True)),
                ('timefield', models.TimeField(null=True)),
                ('urlfield', models.URLField(null=True)),
                ('uuidfield', models.UUIDField(default=uuid.uuid4, null=True)),
                ('sections', wagtail.core.fields.StreamField([('s_smallblock', wagtail.core.blocks.StructBlock([('charblock', wagtail.core.blocks.CharBlock()), ('textblock', wagtail.core.blocks.TextBlock()), ('emailblock', wagtail.core.blocks.EmailBlock())])), ('s_bigblock', wagtail.core.blocks.StructBlock([('integerblock', wagtail.core.blocks.IntegerBlock()), ('floatblock', wagtail.core.blocks.FloatBlock()), ('decimalblock', wagtail.core.blocks.DecimalBlock()), ('regexblock', wagtail.core.blocks.RegexBlock(regex='')), ('urlblock', wagtail.core.blocks.URLBlock()), ('booleanblock', wagtail.core.blocks.BooleanBlock()), ('dateblock', wagtail.core.blocks.DateBlock())])), ('s_tallblock', wagtail.core.blocks.StructBlock([('timeblock', wagtail.core.blocks.TimeBlock()), ('datetimeblock', wagtail.core.blocks.DateTimeBlock()), ('richtextblock', wagtail.core.blocks.RichTextBlock()), ('rawhtmlblock', wagtail.core.blocks.RawHTMLBlock()), ('blockquoteblock', wagtail.core.blocks.BlockQuoteBlock()), ('choiceblock', wagtail.core.blocks.ChoiceBlock(choices=[('apples', 'Apple'), ('bananas', 'Bananas')]))])), ('s_lightblock', wagtail.core.blocks.StructBlock([('documentchooserblock', wagtail.documents.blocks.DocumentChooserBlock()), ('imagechooserblock', wagtail.images.blocks.ImageChooserBlock()), ('snippetchooserblock', wagtail.snippets.blocks.SnippetChooserBlock(target_model='utils.Button')), ('embedblock', wagtail.embeds.blocks.EmbedBlock())]))], null=True)),
                ('imagefield', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='images.CustomImage')),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
    ]
