# Generated by Django 3.2.4 on 2021-07-05 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_alter_loja_estoque'),
    ]

    operations = [
        migrations.AddField(
            model_name='estoque',
            name='nome',
            field=models.TextField(null=True),
        ),
    ]
