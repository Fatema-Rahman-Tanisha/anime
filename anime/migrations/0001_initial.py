# Generated by Django 3.2.7 on 2021-10-26 19:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='anime',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('type', models.CharField(max_length=100)),
                ('details', models.TextField()),
                ('poster', models.TextField()),
                ('playlist', models.TextField()),
            ],
        ),
    ]
