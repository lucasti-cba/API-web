from django.contrib import admin
from django.urls import path, include
from . import views
from rest_framework import routers

urlpatterns = [
    path('', views.index, name ='index'),
    path('work/', views.workhome, name ='workhome'),
    path('Cadastros/', views.cadastros, name ='cadastros'),
    path('Cadastro-Medico/', views.cadastroMedico, name ='cadastroMedico'),
    path('Cadastro-Exame/', views.cadastroExame, name ='cadastroExame'),
    path('Cadastro-Paciente/', views.cadastroPaciente, name ='cadastroPaciente'),
    path('Novo-Exame/<int:paciente>/', views.exameRealizado, name ='exameRealizado'),
    path('relatorios/', views.relatorios, name ='relatorios'),
    path('relatoriosData/', views.relatoriosData, name ='relatoriosData'),
    path('relatoriosDataMedico/', views.relatoriosDataMedico, name ='relatoriosDataMedico'),
    path('relatoriosDataCSV/', views.relatoriosDataCSV, name ='relatoriosDataCSV'),
    path('select/', views.selectPaciente, name='selectPaciente'),
    path('caixaAbrir/', views.caixaAbrir, name='caixaAbrir'),
    path('caixaAbrirUser/', views.caixaAbrirUser, name='caixaAbrirUser'),
    path('recebimentoAt/<int:atendimento>', views.recebimentoAt, name='recebimentoAt'),
]

