# Generated by Django 3.2.4 on 2021-08-13 17:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('unimagem', '0006_examerealizado_author'),
    ]

    operations = [
        migrations.CreateModel(
            name='Recebimento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.TextField()),
                ('valor', models.FloatField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Caixa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hora_abertura', models.DateTimeField()),
                ('valor_abertura', models.FloatField()),
                ('hora_fechamento', models.DateTimeField()),
                ('valor_fechamento', models.FloatField()),
                ('fechamento_justificativa', models.TextField(blank=True, null=True)),
                ('atendimento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='unimagem.examerealizado')),
                ('recebimento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='unimagem.recebimento')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
