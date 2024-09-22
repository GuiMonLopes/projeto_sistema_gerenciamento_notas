from django.shortcuts import render

def index(request):
        return render(request, 'login/index.html')

def cadastro(request):
        return render(request, 'login/cadastro.html')