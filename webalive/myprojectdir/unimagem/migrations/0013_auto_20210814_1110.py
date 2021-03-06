# Generated by Django 3.2.4 on 2021-08-14 14:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('unimagem', '0012_alter_recebimento_tipo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Paciente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.TextField()),
                ('cpf', models.TextField()),
                ('data_nascimento', models.DateTimeField()),
                ('nome_mae', models.TextField()),
                ('telefone', models.TextField()),
                ('email', models.TextField()),
            ],
        ),
        migrations.RenameField(
            model_name='examerealizado',
            old_name='author',
            new_name='user',
        ),
        migrations.RemoveField(
            model_name='examerealizado',
            name='cpf',
        ),
        migrations.RemoveField(
            model_name='examerealizado',
            name='data_nascimento',
        ),
        migrations.RemoveField(
            model_name='examerealizado',
            name='nome_mae',
        ),
        migrations.AddField(
            model_name='recebimento',
            name='recebimento_justificativa',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='examerealizado',
            name='paciente',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='unimagem.paciente'),
        ),
    ]
