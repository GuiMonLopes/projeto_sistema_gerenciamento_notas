from django.contrib import admin

from login.models import Aluno, Professor

class AlunoAdmin(admin.ModelAdmin):
    list_display = ['nome', 'data_nascimento', 'email', 'telefone']
    search_fields = ['nome', 'email']
    # Você pode incluir outras configurações, como campos de filtro

admin.site.register(Aluno, AlunoAdmin)
admin.site.register(Professor)
