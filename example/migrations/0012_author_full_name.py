# Generated by Django 4.1 on 2022-09-06 15:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("example", "0011_rename_type_author_author_type_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="author",
            name="full_name",
            field=models.CharField(default="", max_length=50),
            preserve_default=False,
        ),
    ]