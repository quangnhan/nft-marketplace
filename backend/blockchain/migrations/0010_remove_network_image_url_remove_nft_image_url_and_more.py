# Generated by Django 5.0.2 on 2024-04-19 15:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blockchain', '0009_nft_uri_alter_smartcontract_image_url_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='network',
            name='image_url',
        ),
        migrations.RemoveField(
            model_name='nft',
            name='image_url',
        ),
        migrations.RemoveField(
            model_name='smartcontract',
            name='image_url',
        ),
    ]
