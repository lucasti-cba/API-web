from django.db import models
from django.contrib.auth.models import User

TYPE_CHOICES = [
    ('Dinheiro', 'Dinheiro'),
    ('Cartão Débito', 'Cartão Débito'),
    ('Cartão Crédito', 'Cartão Crédito'),
    ('PIX', 'PIX'),
    ('Cheque', 'Cheque'),
    ('Transferência Bancaria','Transferência Bancaria' ),
    ('Unimed-CBA', 'Unimed-CBA'),
    ('Unimed-NACIONAL', 'Unimed-NACIONAL'),
    ('Unimed-FACIL', 'Unimed-FACIL'),
    ('Unimed-MAIS', 'Unimed-MAIS'),
    ('PAX', 'PAX'),    
    ('BRADESCO', 'BRADESCO'),
    ('OUTROS', 'OUTROS'),
]
# Create your models here.
class Paciente(models.Model):
    nome = models.TextField( blank=False, null=False)
    cpf = models.TextField( blank=False, null=False)
    data_nascimento = models.DateField()
    nome_mae = models.TextField( blank=False, null=False)
    telefone = models.TextField( blank=False, null=False)
    email = models.TextField( blank=False, null=False)
    def __str__(self):
        return self.nome

class Medico(models.Model):
    nome = models.TextField( blank=False, null=False)
    crm = models.TextField( blank=False, null=False)
    especialidade = models.TextField( blank=False, null=False)
    def __str__(self):
        return self.nome

class Exame(models.Model):
    nome = models.TextField( blank=False, null=False)
    codigo = models.TextField( blank=False, null=False)
    valor = models.FloatField( blank=False, null=False)
    valor_repasse = models.FloatField( blank=True, null=True)
    def __str__(self):
        return self.nome

class ExameRealizado(models.Model):
    exame = models.ManyToManyField(Exame)
    medico = models.ForeignKey(Medico, on_delete=models.CASCADE, blank=True, null=True)
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE, blank=True, null=True)   
    data_exame = models.DateTimeField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
 
class Recebimento(models.Model):
    tipo = models.TextField( blank = False, null = False, choices=TYPE_CHOICES)
    valor = models.FloatField( blank = False, null = False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=False, null=False)
    recebimento_justificativa = models.TextField( blank = True, null = True)

class Lancamento(models.Model):
    exames = models.ForeignKey(ExameRealizado, on_delete=models.CASCADE, blank=False, null=False)
    recebimento = models.ForeignKey(Recebimento, on_delete=models.CASCADE, blank=True, null=True)


class Caixa(models.Model):
    atendimento = models.ManyToManyField(Lancamento, blank=True, null=True)
    hora_abertura = models.DateTimeField()
    aberto = models.TextField( blank=True, null=True)
    valor_abertura = models.FloatField( blank = False, null = False)
    hora_fechamento =  models.DateTimeField(blank = True, null = True)
    valor_fechamento = models.FloatField( blank = True, null = True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=False, null=False)
    fechamento_justificativa = models.TextField( blank = True, null = True)