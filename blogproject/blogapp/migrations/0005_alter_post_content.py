# Generated by Django 4.2.1 on 2023-05-26 12:38

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("blogapp", "0004_comment_created_date_comment_text"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post", name="content", field=ckeditor.fields.RichTextField(),
        ),
    ]
