from django.urls import path
from gerenciamento.views import index, incluir_nota, verificar_nota, alunos, turmas

urlpatterns = [
    path('', index, name='gerenciamento'),
    path('incluir_nota/', incluir_nota, name='incluir_nota'),
    path('verificar_nota/', verificar_nota, name='verificar_nota'),
    path('alunos/', alunos, name='alunos'),
    path('turmas/', turmas, name='turmas'),
]