from django.urls import path
from gerenciamento.views import index, incluir_nota, verificar_nota, alunos, turmas

urlpatterns = [
    path('', index),
    path('incluir_nota/', incluir_nota),
    path('verificar_nota/', verificar_nota),
    path('alunos/', alunos),
    path('turmas/', turmas),
]