# Generated by Django 2.2.6 on 2019-10-23 11:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ukr_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='links',
            name='interval',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
