# Generated by Django 2.2.12 on 2020-07-29 20:32

from django.db import migrations, models
import django.db.models.deletion
import wagtail.core.blocks
import wagtail.core.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('wagtailcore', '0045_assign_unlock_grouppagepermission'),
    ]

    operations = [
        migrations.CreateModel(
            name='NavigationSettings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('primary_navigation', wagtail.core.fields.StreamField([('link', wagtail.core.blocks.StructBlock([('page', wagtail.core.blocks.PageChooserBlock()), ('title', wagtail.core.blocks.CharBlock(help_text="Leave blank to use the page's own title", required=False))]))], blank=True, help_text='Main site navigation')),
                ('footer_links', wagtail.core.fields.StreamField([('link', wagtail.core.blocks.StructBlock([('page', wagtail.core.blocks.PageChooserBlock()), ('title', wagtail.core.blocks.CharBlock(help_text="Leave blank to use the page's own title", required=False))]))], blank=True, help_text='Single list of elements at the base of the page.')),
                ('footer_bottom_text', wagtail.core.fields.RichTextField(blank=True, help_text='Small print text at the bottom of all pages. Not required.')),
                ('site', models.OneToOneField(editable=False, on_delete=django.db.models.deletion.CASCADE, to='wagtailcore.Site')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
