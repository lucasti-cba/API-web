# Generated by Django 3.2.4 on 2021-07-05 15:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_estoque_nome'),
    ]

    operations = [
        migrations.AlterField(
            model_name='loja',
            name='estoque',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.estoque'),
        ),
    ]