# Generated by Django 3.1.1 on 2020-09-06 08:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_auto_20200906_0812'),
    ]

    operations = [
        migrations.AlterField(
            model_name='genre',
            name='agelimit',
            field=models.IntegerField(choices=[(1, 'Adult'), (2, 'Young'), (3, 'Children')], null=True),
        ),
    ]
