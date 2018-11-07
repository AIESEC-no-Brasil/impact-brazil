# Generated by Django 2.1.1 on 2018-11-07 19:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0035_city_thumbnail'),
    ]

    operations = [
        migrations.AddField(
            model_name='sdg',
            name='thumbnail',
            field=models.CharField(blank=True, max_length=256, verbose_name='Thumbnail Filename (.jpg)'),
        ),
        migrations.AddField(
            model_name='sdg',
            name='video_link',
            field=models.CharField(blank=True, max_length=256, verbose_name='Video ID (YouTube)'),
        ),
        migrations.AddField(
            model_name='subproduct',
            name='thumbnail',
            field=models.CharField(blank=True, max_length=256, verbose_name='Thumbnail Filename (.jpg)'),
        ),
        migrations.AddField(
            model_name='subproduct',
            name='video_link',
            field=models.CharField(blank=True, max_length=256, verbose_name='Video ID (YouTube)'),
        ),
    ]
