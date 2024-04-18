# Generated by Django 5.0.2 on 2024-04-18 06:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blockchain', '0008_rename_blockchain_network_network_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='nft',
            name='uri',
            field=models.URLField(default=''),
        ),
        migrations.AlterField(
            model_name='smartcontract',
            name='image_url',
            field=models.URLField(blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='smartcontract',
            name='name',
            field=models.CharField(blank=True, default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='smartcontract',
            name='token_symbol',
            field=models.CharField(blank=True, default='', max_length=50),
        ),
    ]
