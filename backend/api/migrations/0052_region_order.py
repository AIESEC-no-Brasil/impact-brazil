# Generated by Django 2.1.2 on 2018-11-28 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0051_lc_searchtool_link'),
    ]

    operations = [
        migrations.AddField(
            model_name='region',
            name='order',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]