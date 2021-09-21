from rest_framework import viewsets
from .models import *
from .serializers import *


class LojaDetail(viewsets.ModelViewSet):
    queryset = Loja.objects.all()
    serializer_class = LojaSerializer

class EnderecoDetail(viewsets.ModelViewSet):
    queryset = Endereco.objects.all()
    serializer_class = EnderecoSerializer