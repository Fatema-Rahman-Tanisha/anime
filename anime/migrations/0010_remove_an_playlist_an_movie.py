# Generated by Django 4.0 on 2022-02-02 19:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('anime', '0009_an_viewsnum'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='an',
            name='playlist',
        ),
        migrations.AddField(
            model_name='an',
            name='movie',
            field=models.FileField(default='', upload_to=''),
        ),
    ]
