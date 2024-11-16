from django.urls import path
from gerenciamento.views import incluir_professor, index, incluir_nota, verificar_nota, alunos, turmas, matricula

urlpatterns = [
    path('', index, name='gerenciamento'),
    path('incluir_nota/', incluir_nota, name='incluir_nota'),
    path('verificar_nota/', verificar_nota, name='verificar_nota'),
    path('alunos/', alunos, name='alunos'),
    path('turmas/', turmas, name='turmas'),
    path('matricula/', matricula, name='matricula'),
    path('incluir_professor/', incluir_professor, name='incluir_professor'),
]