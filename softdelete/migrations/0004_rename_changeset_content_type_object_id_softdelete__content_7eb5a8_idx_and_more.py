# Generated by Django 5.0.7 on 2024-08-12 17:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("softdelete", "0003_auto_20211015_1406"),
    ]

    operations = [
        migrations.RenameIndex(
            model_name="changeset",
            new_name="softdelete__content_7eb5a8_idx",
            old_fields=("content_type", "object_id"),
        ),
        migrations.RenameIndex(
            model_name="softdeleterecord",
            new_name="softdelete__content_faa170_idx",
            old_fields=("content_type", "object_id"),
        ),
    ]
