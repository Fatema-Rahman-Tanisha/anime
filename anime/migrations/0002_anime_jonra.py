# Generated by Django 3.2.7 on 2021-10-26 19:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('anime', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='anime',
            name='jonra',
            field=models.CharField(default='', max_length=100),
        ),
    ]
