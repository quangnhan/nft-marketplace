# Generated by Django 5.0.2 on 2024-04-10 14:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blockchain', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='smartcontract',
            old_name='name',
            new_name='chain_name',
        ),
        migrations.RenameField(
            model_name='smartcontract',
            old_name='chain',
            new_name='network',
        ),
    ]
