# Generated by Django 4.0 on 2022-02-03 17:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('anime', '0012_an_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='favourite',
            name='anime',
            field=models.ManyToManyField(to='anime.AN'),
        ),
        migrations.DeleteModel(
            name='Item',
        ),
    ]
