from django.shortcuts import render

def index(request):
        return render(request, 'gerenciamento/index.html')

def alunos(request):
        return render(request, 'gerenciamento/alunos.html')

def turmas(request):
        return render(request, 'gerenciamento/turmas.html')

def incluir_nota(request):
        return render(request, 'gerenciamento/incluir_nota.html')

def verificar_nota(request):
        return render(request, 'gerenciamento/verificar_nota.html')