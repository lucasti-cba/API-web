from django.contrib import admin
from .models import *

admin.site.register(Paciente)
admin.site.register(Medico)
admin.site.register(Exame)
admin.site.register(ExameRealizado)
admin.site.register(Caixa)
admin.site.register(Lancamento)
admin.site.register(Recebimento)