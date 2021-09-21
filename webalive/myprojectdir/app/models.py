from django.db import models
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.models import User


class Imagem(models.Model):
	imagens = models.ImageField(upload_to='images/', blank=False, null=False)


class Endereco(models.Model):
    CEP = models.TextField( blank=False, null=False)
    logradouro = models.TextField( blank=False, null=False)
    numero = models.TextField( blank=False, null=False)
    complemento = models.TextField( blank=False, null=False)
    bairro = models.TextField( blank=False, null=False)
    cidade = models.TextField( blank=False, null=False)
    uf = models.TextField( blank=False, null=False)
    pais = models.TextField( blank=False, null=False)
    def __str__(self):
        return self.CEP

class TagProduto(models.Model):
    tag =  models.TextField( blank=False, null=False)
    def __str__(self):
        return self.tag

class Produto(models.Model):
    nome = models.TextField( blank=False, null=False)
    imagens = models.ForeignKey(Imagem,on_delete=models.CASCADE, blank=False, null=False) 
    valor = models.FloatField(blank=False, null=False)
    descricao = models.TextField( blank=False, null=False)
    tags = models.ForeignKey(TagProduto,on_delete=models.CASCADE, blank=False, null=False) 
    def __str__(self):
        return self.nome

class EstoqueAtivo(models.Model):
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE, blank=False, null=False) 
    quantidade = models.IntegerField(blank=False, null=False)
    def __str__(self):
        return self.produto.nome


class Estoque(models.Model):
    nome =  models.TextField( blank=False, null=True)
    produto =  models.ManyToManyField(EstoqueAtivo)
    def __str__(self):
        return self.nome

class Loja(models.Model):
    dono = models.OneToOneField(User, on_delete=models.SET_NULL, null=True)
    nome = models.TextField( blank=False, null=False)
    logo = models.OneToOneField(Imagem, on_delete=models.SET_NULL, null=True)
    endereco = models.OneToOneField(Endereco, on_delete=models.SET_NULL, null=True)
    estoque =  models.ForeignKey(Estoque,on_delete=models.CASCADE, blank=True, null=True) 
    def __str__(self):
        return self.nome


