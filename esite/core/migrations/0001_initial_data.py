# -*- coding: utf-8 -*-
from django.db import migrations


def create_homepage(apps, schema_editor):
    # Get models
    ContentType = apps.get_model("contenttypes.ContentType")
    Page = apps.get_model("wagtailcore.Page")
    Site = apps.get_model("wagtailcore.Site")
    Image = apps.get_model("wagtailimages.Image")

    # Delete the default homepage
    # If migration is run multiple times, it may have already been deleted
    Page.objects.filter(id=2).delete()

    # Create page content type
    page_content_type, created = ContentType.objects.get_or_create(
        model="page", app_label="wagtailcore"
    )

    # Create root page
    # root = Page.objects.create(
    #     title="Root",
    #     slug='root',
    #     content_type=page_content_type,
    #     path='0001',
    #     depth=1,
    #     numchild=1,
    #     url_path='/',
    # )

    # Create homepage
    homepage = Page.objects.create(
        title="OPS",
        slug="home",
        content_type=page_content_type,
        path="00010001",
        depth=2,
        numchild=0,
        url_path="/home/",
    )

    # Create default site
    Site.objects.create(
        hostname="localhost", root_page_id=homepage.id, is_default_site=True
    )


def remove_homepage(apps, schema_editor):
    # Get models
    ContentType = apps.get_model("contenttypes.ContentType")
    HomePage = apps.get_model("home.HomePage")

    # Delete the default homepage
    # Page and Site objects CASCADE
    HomePage.objects.filter(slug="home", depth=2).delete()

    # Delete content type for homepage model
    ContentType.objects.filter(model="homepage", app_label="home").delete()


class Migration(migrations.Migration):

    dependencies = [
        ("wagtailimages", "0001_initial"),
    ]

    operations = [
        migrations.RunPython(create_homepage, remove_homepage),
    ]
