# Generated by Django 3.2.4 on 2021-08-13 20:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('unimagem', '0010_auto_20210813_1654'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='examerealizado',
            name='exame',
        ),
        migrations.AddField(
            model_name='examerealizado',
            name='exame',
            field=models.ManyToManyField(to='unimagem.Exame'),
        ),
    ]
