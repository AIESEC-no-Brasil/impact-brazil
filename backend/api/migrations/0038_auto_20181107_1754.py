# Generated by Django 2.1.1 on 2018-11-07 19:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0037_product_details'),
    ]

    operations = [
        migrations.AddField(
            model_name='sdg',
            name='description',
            field=models.TextField(blank=True, verbose_name='SDG Description'),
        ),
        migrations.AddField(
            model_name='subproduct',
            name='description',
            field=models.TextField(blank=True, verbose_name='Subproduct Description'),
        ),
    ]
