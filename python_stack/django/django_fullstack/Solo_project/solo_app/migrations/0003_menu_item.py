# Generated by Django 3.2 on 2021-06-10 01:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('solo_app', '0002_rename_email_address_user_email'),
    ]

    operations = [
        migrations.CreateModel(
            name='Menu_item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_name', models.CharField(max_length=255)),
                ('price', models.DecimalField(decimal_places=2, max_digits=5)),
                ('description', models.TextField()),
                ('image', models.CharField(blank=True, max_length=5000, null=True)),
            ],
        ),
    ]
