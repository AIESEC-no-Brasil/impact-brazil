# Generated by Django 2.1.1 on 2018-11-07 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0034_city_video_link'),
    ]

    operations = [
        migrations.AddField(
            model_name='city',
            name='thumbnail',
            field=models.CharField(blank=True, max_length=256, verbose_name='Thumbnail Filename (.jpg)'),
        ),
    ]
