# Generated by Django 2.0.5 on 2018-10-29 04:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Acted',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Actor',
            fields=[
                ('actorid', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30)),
                ('photo', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('movieId', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=30)),
                ('year', models.CharField(max_length=4)),
                ('length', models.CharField(max_length=10)),
                ('genres', models.CharField(max_length=100)),
                ('rate', models.IntegerField(default=0)),
                ('poster', models.CharField(max_length=500)),
            ],
        ),
        migrations.AddField(
            model_name='acted',
            name='actorid',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='movies.Movie'),
        ),
        migrations.AddField(
            model_name='acted',
            name='movieid',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='movies.Actor'),
        ),
    ]
