# Generated by Django 3.2.4 on 2021-08-16 18:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('unimagem', '0018_alter_lancamento_recebimento'),
    ]

    operations = [
        migrations.AlterField(
            model_name='caixa',
            name='atendimento',
            field=models.ManyToManyField(blank=True, null=True, to='unimagem.Lancamento'),
        ),
        migrations.AlterField(
            model_name='recebimento',
            name='tipo',
            field=models.TextField(choices=[('Dinheiro', 'Dinheiro'), ('Cartão Débito', 'Cartão Débito'), ('Cartão Crédito', 'Cartão Crédito'), ('PIX', 'PIX'), ('Cheque', 'Cheque'), ('Transferência Bancaria', 'Transferência Bancaria'), ('Unimed-CBA', 'Unimed-CBA'), ('Unimed-NACIONAL', 'Unimed-NACIONAL'), ('Unimed-FACIL', 'Unimed-FACIL'), ('Unimed-MAIS', 'Unimed-MAIS'), ('PAX', 'PAX'), ('BRADESCO', 'BRADESCO'), ('OUTROS', 'OUTROS')]),
        ),
    ]
