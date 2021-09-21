from django.contrib import admin
from .models import *


admin.site.register(Loja)
admin.site.register(Produto)
admin.site.register(Endereco)
admin.site.register(Imagem)
admin.site.register(TagProduto)
admin.site.register(Estoque)
admin.site.register(EstoqueAtivo)