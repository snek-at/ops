# Generated by Django 2.2.12 on 2020-08-01 00:15

from django.db import migrations
import django.db.models.deletion
import modelcluster.fields


class Migration(migrations.Migration):

    dependencies = [
        ('ops_pipelines', '0003_auto_20200801_0209'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pipelineformfield',
            name='page',
            field=modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='form_fields', to='ops_pipelines.PipelineFormPage'),
        ),
    ]
