# Generated by Django 3.0.5 on 2020-12-07 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Point',
            fields=[
                ('point', models.FloatField(default=0, max_length=30, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Speciality',
            fields=[
                ('name', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('points', models.ManyToManyField(default=0, to='main.Point')),
            ],
        ),
        migrations.CreateModel(
            name='Study',
            fields=[
                ('form', models.CharField(max_length=30, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Univer',
            fields=[
                ('name', models.CharField(blank=True, max_length=30, primary_key=True, serialize=False)),
                ('rating', models.FloatField(default=0, max_length=10)),
                ('address', models.CharField(default='Almaty', max_length=100)),
                ('description', models.CharField(max_length=500)),
                ('news', models.CharField(blank=True, max_length=500)),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('form_of_study', models.ManyToManyField(default='full-time', to='main.Study')),
                ('specialities', models.ManyToManyField(default='default', to='main.Speciality')),
            ],
        ),
    ]