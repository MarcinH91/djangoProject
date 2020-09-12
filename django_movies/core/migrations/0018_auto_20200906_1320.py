# Generated by Django 3.1.1 on 2020-09-06 13:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0017_auto_20200906_1021'),
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', models.CharField(max_length=40, null=True, unique=True)),
            ],
            options={
                'ordering': ['country'],
            },
        ),
        migrations.AlterField(
            model_name='movie',
            name='category',
            field=models.CharField(max_length=100, null=True, unique=True),
        ),
        migrations.AlterUniqueTogether(
            name='movie',
            unique_together={('title', 'released')},
        ),
        migrations.AddField(
            model_name='movie',
            name='countries',
            field=models.ManyToManyField(related_name='movies', to='core.Country'),
        ),
    ]
