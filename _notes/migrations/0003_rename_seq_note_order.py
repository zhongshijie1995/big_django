# Generated by Django 3.2.5 on 2021-11-22 16:05

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ('_notes', '0002_rename_notes_note'),
    ]

    operations = [
        migrations.RenameField(
            model_name='note',
            old_name='seq',
            new_name='order',
        ),
    ]
