# Generated by Django 2.1.2 on 2018-11-28 20:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0052_region_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='city',
            name='hidden',
            field=models.BooleanField(default=False),
        ),
    ]
