# Generated by Django 3.0.5 on 2020-12-07 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='speciality',
            name='points',
            field=models.ManyToManyField(to='main.Point'),
        ),
    ]
