from django import forms
from .models import *
from django.forms import ModelForm

class CadastroMedico_Form(forms.Form):
	nome = forms.CharField(label='nome', max_length=250)
	crm = forms.CharField(label="crm", max_length=15)
	especialidade = forms.CharField(label='especialidade', max_length=50)

class Pessoa_Form(ModelForm):
    class Meta:
        model = Paciente
        fields = ['nome', 'cpf', 'data_nascimento','nome_mae', 'email' , 'telefone']

class Pesquisa_Form(forms.Form):
	pesquisa = forms.CharField(label='pesquisa', max_length=250)

class Select_Form(forms.Form):
    select = forms.IntegerField(label='pesquisa')
    
class CadastroExame_Form(forms.Form):
	nome = forms.CharField(label='nome', max_length=250)
	codigo = forms.CharField(label="codigo", max_length=15)
	valor = forms.FloatField(label='valor')

class ExameRealizado_Form(ModelForm):
    class Meta:
        model = ExameRealizado
        fields = ['exame', 'medico',]
        exame =  forms.ModelMultipleChoiceField(
        queryset=Exame.objects.all(),
        widget=forms.CheckboxSelectMultiple(  ),

    )
        widgets = {
            'medico': forms.Select(attrs={'class': 'form-control'}), 
            'paciente': forms.Select(attrs={'class': 'form-control'}), 

        }

class RelatorioData_Form(forms.Form):
    dataIni = forms.DateField()
    dataFin = forms.DateField()

class RelatorioDataMedico_Form(forms.Form):

    dataIni = forms.DateField()
    dataFin = forms.DateField()
    medico = forms.CharField(label='Médico', max_length=15)



class Recebimento_Form(ModelForm):
    class Meta:
        model = Recebimento
        fields = ['tipo', 'valor', 'recebimento_justificativa']
        widgets = {
            'tipo': forms.Select(attrs={'class': 'form-control'}), 
            'valor': forms.NumberInput(attrs={'class': 'form-control'}),
            'recebimento_justificativa': forms.Textarea(attrs={'class': 'form-control'}),  
        }

class AbrirCForm(forms.Form):
    aberto = forms.CharField(label='aberto', max_length=1)
