from django.shortcuts import render, redirect, get_object_or_404
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
from .serializers import *

register = Library()


class LojaDetail(viewsets.ModelViewSet):
    queryset = Loja.objects.values_list('nome', 'logo__imagens')
    serializer_class = LojaSerializer


def index(request):
    return render(request, 'Site1/Home.html')

def cadastrar_usuario(request):
	if request.method == "POST":
	    form_usuario = UserCreationForm(request.POST)
	    if form_usuario.is_valid():
	        form_usuario.save()
	        username = form_usuario.cleaned_data['username']
	        password = form_usuario.cleaned_data['password1']
	        usuario = authenticate(request, username=username, password=password)
	        if usuario is not None:
	            auth_login(request, usuario)
	            return redirect('dadospessoais')
	    else:
	    	return render(request, 'cadastro_user.html', {'form': form_usuario, 'title': 'Criar Conta', })

	form = UserCreationForm()	
	return render(request, 'cadastro_user.html', {'form': form, 'title': 'Criar Conta', })




def logar_usuario(request):
    mensagem = None 
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        usuario = authenticate(request, username=username, password=password)
        if usuario is not None:
            auth_login(request, usuario)
            user = request.user.id
            try:
	            dados = Dados_pessoais.objects.get(user=user)	         
	            return redirect('index')
            except:
            	return redirect('dadospessoais')
        else:
        	mensagem = 'Usuario ou senha invalido.'
    return render(request, 'Site1/Login.html', {'mensagem':mensagem, 'title':'Login', })




def logout(request):
    auth_logout(request)
    return redirect('index')

