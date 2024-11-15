from django.contrib import admin

from gerenciamento.models import Turma, Matricula, Nota

admin.site.register(Turma)
admin.site.register(Matricula)
admin.site.register(Nota)