# Generated by Django 3.2 on 2021-05-17 05:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books_authors_app', '0002_author_notes'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='desc',
            new_name='description',
        ),
    ]
