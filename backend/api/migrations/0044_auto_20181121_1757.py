# Generated by Django 2.1.2 on 2018-11-21 19:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0043_auto_20181121_1515'),
    ]

    operations = [
        migrations.AlterField(
            model_name='focus',
            name='lc',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.LC', to_field='gis_id'),
        ),
    ]
