# Generated by Django 5.1.3 on 2024-11-22 10:32

import wagtail.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0002_create_homepage"),
    ]

    operations = [
        migrations.AddField(
            model_name="homepage",
            name="body",
            field=wagtail.fields.RichTextField(blank=True),
        ),
    ]
