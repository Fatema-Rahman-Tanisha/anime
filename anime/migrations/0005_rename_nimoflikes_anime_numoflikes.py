# Generated by Django 3.2.7 on 2021-10-30 19:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('anime', '0004_anime_nimoflikes'),
    ]

    operations = [
        migrations.RenameField(
            model_name='anime',
            old_name='NimOfLikes',
            new_name='NumOfLikes',
        ),
    ]
