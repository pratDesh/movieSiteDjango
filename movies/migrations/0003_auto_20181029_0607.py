# Generated by Django 2.0.5 on 2018-10-29 06:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0002_auto_20181029_0547'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='plot',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='movie',
            name='rate',
            field=models.FloatField(default=0),
        ),
    ]
