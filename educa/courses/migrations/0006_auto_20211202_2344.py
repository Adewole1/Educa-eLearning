# Generated by Django 3.2.9 on 2021-12-02 23:44

import autoslug.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0005_auto_20211202_2341'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='slug',
            field=autoslug.fields.AutoSlugField(editable=True, populate_from='title', unique=True),
        ),
        migrations.AlterField(
            model_name='subject',
            name='slug',
            field=autoslug.fields.AutoSlugField(editable=True, populate_from='title', unique=True),
        ),
    ]