from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, authenticate
from django.contrib.auth import (
    REDIRECT_FIELD_NAME, get_user_model, login as auth_login,
    logout as auth_logout, update_session_auth_hash,
)
from .models import *
from .forms import *
import os
import time
from django.template import Library
from django.core.files.uploadedfile import SimpleUploadedFile
from datetime import datetime
from urllib.parse import urlencode
import json
from functools import wraps
import jwt
from django.conf import settings
from django.http import Http404, JsonResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout as log_out
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status, viewsets
import pytz
import csv

register = Library()

def querySet_to_list(qs):
    """
    this will return python list<dict>
    """
    return [dict(q) for q in qs]

def index(request):
    user = request.user.id
    if user is not None:
        return redirect('workhome')

    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        usuario = authenticate(request, username=username, password=password)
        if usuario is not None:
            auth_login(request, usuario)
            user = request.user.id
        else:
        	mensagem = 'Usuario ou senha invalido.'
    return render(request, 'unimagem/home.html')

def workhome(request):
    user = request.user.id
    try:
        caixa = get_object_or_404(Caixa, user=request.user , aberto='A')
    except:
        caixa = None
    if caixa is  None:
        return redirect('caixaAbrir')
    if user is  None:
        return redirect('index')

    return render(request, 'unimagem/workhome.html')

def cadastros(request):
    user = request.user
    if user is  None:
        return redirect('index')
    return render(request, 'unimagem/cadastros.html')

def cadastroPaciente(request):
    user = request.user
    if user is  None:
        return redirect('index')
    form = Pessoa_Form()
    if request.method == "POST":
        form = Pessoa_Form(request.POST)
        if form.is_valid():
            nome = form.cleaned_data['nome']
            cpf = form.cleaned_data['cpf']
            data_nascimento = form.cleaned_data['data_nascimento']
            nome_mae = form.cleaned_data['nome_mae']
            email = form.cleaned_data['email']
            telefone = form.cleaned_data['telefone']
            paciente = Paciente(nome=nome, cpf= cpf, data_nascimento=data_nascimento, nome_mae = nome_mae, email = email, telefone = telefone  )
            paciente.save()
            return redirect('workhome')
        else:
            return HttpResponse('Error')

    return render(request, 'unimagem/cadastro-paciente.html', { 'form' : form, })

def cadastroMedico(request):
    user = request.user
    if user is  None:
        return redirect('index')
    if request.method == "POST":
        form = CadastroMedico_Form(request.POST)
        if form.is_valid():
            nome = form.cleaned_data['nome']
            crm = form.cleaned_data['crm']
            especialidade = form.cleaned_data['especialidade']
            medico = Medico(nome=nome, crm= crm, especialidade=especialidade)
            medico.save()
            return redirect('workhome')
    return render(request, 'unimagem/cadastro-medico.html')

def cadastroExame(request):
    user = request.user
    if user is  None:
        return redirect('index')  
    if request.method == "POST":
        form = CadastroExame_Form(request.POST)
        if form.is_valid():
            nome = form.cleaned_data['nome']
            codigo = form.cleaned_data['codigo']
            valor = form.cleaned_data['valor']
            exame = Exame(nome=nome, codigo= codigo, valor=valor)
            exame.save()
            return redirect('workhome')

    return render(request, 'unimagem/cadastro-exame.html')

def selectPaciente(request):
    user = request.user.id
    try:
        caixa = get_object_or_404(Caixa, user=request.user , aberto='A')
    except:
        caixa = None
    if caixa is  None:
        return redirect('caixaAbrir')
    if user is  None:
        return redirect('index')
    names = 'False'
    form = Pesquisa_Form()
    if request.method == "POST":
        form = Pesquisa_Form(request.POST)
        if form.is_valid():
            search = form.cleaned_data['pesquisa']
            pesquisa = Paciente.objects.filter(nome__icontains=search) or Paciente.objects.filter(cpf__icontains=search)
            return render(request, 'unimagem/selectPaciente.html', {'names':'True', 'query': pesquisa , 'mensagem':pesquisa})

    return render(request, 'unimagem/selectPaciente.html', { 'names': names})

def exameRealizado(request, paciente):
    form = ExameRealizado_Form()
    paciente = get_object_or_404(Paciente, id=paciente)
    if request.method == "POST":
        selectForm = Select_Form(request.POST)
        form = ExameRealizado_Form(request.POST)
        if form.is_valid():
            exameR = form.cleaned_data['exame']
            medico = form.cleaned_data['medico']
            data_exame = datetime.now(pytz.timezone('America/Cuiaba'))
            exame = ExameRealizado( medico= medico, paciente = paciente,  data_exame = data_exame, user = request.user  )
            exame.save()
            total = 0
            for e in exameR:
                total += e.valor
                exame.exame.add(e)
                exame.save()
            form = Recebimento_Form
            atendimento = Lancamento(exames  = exame)
            atendimento.save()     
            return render(request, 'unimagem/recebimento.html', { 'exame': exame, 'total':total , 'form':form, 'atendimento':atendimento})
    return render(request, 'unimagem/novo-exame.html', { 'form': form , 'paciente':paciente })

def recebimentoAt(request, atendimento):
    user = request.user
    if user is  None:
        return redirect('index')
    try:
        caixa = get_object_or_404(Caixa, user=request.user , aberto='A')
    except:
        return redirect('caixaAbrir')
    atendimento = get_object_or_404(Lancamento, id=atendimento)
    if request.method == "POST":
        form = Recebimento_Form(request.POST)
        if form.is_valid():
            tipo = form.cleaned_data['tipo']
            valor = form.cleaned_data['valor']
            recebimento_justificativa = form.cleaned_data['recebimento_justificativa']
            recebimento = Recebimento( tipo= tipo, valor = valor,  recebimento_justificativa = recebimento_justificativa, user = request.user  )
            recebimento.save()
            atendimento.recebimento = recebimento
            atendimento.save()
            caixa.atendimento.add(atendimento)
            try:
                caixa.valor_fechamento += valor
            except:
                caixa.valor_fechamento = valor
            caixa.save()   
            return render(request, 'unimagem/recibo.html', { 'atendimento':atendimento})


    return 
def caixaAbrirUser(request):
    caixa = Caixa(hora_abertura = datetime.now(), aberto = 'A', valor_abertura=0, user = request.user )
    caixa.save()
    return redirect('caixaAbrir')     

def caixaAbrir(request):
    user = request.user
    if user is  None:
        return redirect('index')
    try:
        dinheiro = 0
        outros = 0
        caixa = get_object_or_404(Caixa, user=request.user , aberto='A')

    except:
        caixa = None
    if request.method == "POST":
        if caixa == None:        
            caixa = Caixa(hora_abertura = datetime.now(), aberto = 'A', valor_abertura=0, user = request.user )
            caixa.save()           
            return redirect('index')

        else:
            caixa.hora_fechamento = datetime.now()
            caixa.aberto = 'F'
            caixa.save()
            return redirect('index')
    return render(request, 'unimagem/caixa.html', { 'caixa':caixa })

def relatorios(request):
    user = request.user
    if user is  None:
        return redirect('index')
    return render(request, 'unimagem/relatorios.html')

def relatoriosData(request):
    user = request.user
    if user is  None:
        return redirect('index')
    form = RelatorioData_Form()
    rela = False
    if request.method == "POST":
        form = RelatorioData_Form(request.POST)
        if form.is_valid():
            dataIni = form.cleaned_data['dataIni']
            dataFin = form.cleaned_data['dataFin']
            exames = ExameRealizado.objects.filter(data_exame__range=[dataIni, dataFin])
            rela = True

            return render (request, 'unimagem/relatoriosData.html', { 'exames': exames, 'rela':rela})
    return render (request, 'unimagem/relatoriosData.html', {'rela': rela})

def relatoriosDataMedico(request):
    user = request.user
    if user is  None:
        return redirect('index')
    form = RelatorioDataMedico_Form()
    med = Medico.objects.all()
    rela = False
    if request.method == "POST":
        form = RelatorioDataMedico_Form(request.POST)
        if form.is_valid():
            dataIni = form.cleaned_data['dataIni']
            dataFin = form.cleaned_data['dataFin']
            medico = form.cleaned_data['medico']
            medico = Medico.objects.get(id = int(medico))
            exames = ExameRealizado.objects.filter(data_exame__range=[dataIni, dataFin], medico=medico)
            rela = True
            tot = 0
            for e in exames:
               for exa in e.exame.all():
                   tot += 1


            return render (request, 'unimagem/relatoriosMedico.html', { 'exames': exames, 'rela':rela, 'med':med, 'tot':tot})
    return render (request, 'unimagem/relatoriosMedico.html', {'rela': rela, 'med':med})

def relatoriosDataCSV(request):
    user = request.user
    if user is  None:
        return redirect('index')
    # Create the HttpResponse object with the appropriate CSV header.
    response = HttpResponse(
        content_type='text/csv',
        headers={'Content-Disposition': 'attachment; filename="somefilename.csv"'},
    )

    writer = csv.writer(response, delimiter =';')
    form = RelatorioData_Form()
    if request.method == "POST":
        form = RelatorioData_Form(request.POST)
        if form.is_valid():
            dataIni = form.cleaned_data['dataIni']
            dataFin = form.cleaned_data['dataFin']
            query = ExameRealizado.objects.filter(data_exame__range=[dataIni, dataFin])
            writer.writerow(['Exame', 'Solicitante', 'Paciente', 'Data'])
            for e in query:                
                for exame in e.exame.all():
                    writer.writerow([exame.nome, e.medico.nome, e.paciente.nome, e.data_exame.strftime("%m/%d/%Y, %H:%M:%S")])

        return response
    return render (request, 'unimagem/relatoriosDataCSV.html',)