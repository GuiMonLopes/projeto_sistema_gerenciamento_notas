from django.shortcuts import render
from django.views.generic.edit import FormView
from django.views.generic import ListView
from login.models import Aluno
from .models import Turma, Nota, Matricula
from .forms import AlunoForm, TurmaForm, NotaForm, MatriculaForm


def index(request):
    return render(request, 'gerenciamento/index.html')


def alunos(request):
    if request.method == 'POST':
        form = AlunoForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = AlunoForm()  # Formulário vazio para GET

    return render(request, 'gerenciamento/alunos.html', {'form': form})


def turmas(request):
    if request.method == 'POST':
        form = TurmaForm(request.POST)
        if form.is_valid():
            form.save()

    else:
        form = TurmaForm()

    return render(request, 'gerenciamento/turmas.html', {'form': form})


def incluir_nota(request):
    if request.method == 'POST':
        turma_id = request.POST.get('turma')  # Agora pega o ID da turma
        turma = Turma.objects.get(id=turma_id)  # Obtém a turma usando o ID

        # Filtra os alunos pela turma selecionada
        alunos = Aluno.objects.filter(turma=turma)
        for aluno in alunos:
            # Obtém a nota para cada aluno
            nota = request.POST.get(f'nota_{aluno.id}')
            if nota:
                matricula = Matricula.objects.get(
                    aluno=aluno, turma=turma)  # Encontre a matrícula
                # Cria a nota para o aluno
                Nota.objects.create(matricula=matricula, nota=nota)

    turmas = Turma.objects.all()  # Carrega todas as turmas para o formulário
    return render(request, 'gerenciamento/incluir_nota.html', {'turmas': turmas, 'alunos': alunos})


'''def incluir_nota(request):
        if request.method == 'POST':
                turma_id = request.POST['turma_id']
                turma = Turma.objects.get(id=turma_id)
        
                alunos = Aluno.objects.filter(turma=turma)
        
                form = NotaForm(request.POST)
                if form.is_valid():
                        for aluno in alunos:
                                nota = form.cleaned_data[f'nota_{aluno.id}']
                                Nota.objects.create(matricula=Matricula.objects.get(aluno=aluno, turma=turma), nota=nota)
        else:
                turmas = Turma.objects.all()
                alunos = Aluno.objects.all()  # Pode filtrar por turma se necessário
                return render(request, 'gerenciamento/incluir_nota.html', {'turmas': turmas, 'alunos': alunos})'''


def verificar_nota(request):
    turmas = Turma.objects.all()  # Recupera todas as turmas
    notas = None  # Inicializa a variável de notas

    if request.method == 'POST':
        # Pega o ID da turma do formulário
        turma_id = request.POST.get('turma_id')
        # Busca a turma com o ID selecionado
        turma = Turma.objects.get(id=turma_id)
        # Recupera as notas dessa turma
        notas = Nota.objects.filter(matricula__turma=turma)

    return render(request, 'gerenciamento/verificar_nota.html', {'turmas': turmas, 'notas': notas})


def matricula(request):
    if request.method == 'POST':
        form = MatriculaForm(request.POST)
        if form.is_valid():
            form.save()  # Cria a matrícula
    else:
        form = MatriculaForm()

    turmas = Turma.objects.all()  # Carrega todas as turmas
    alunos = Aluno.objects.all()  # Carrega todos os alunos
    return render(request, 'gerenciamento/matricula.html', {'form': form, 'alunos': alunos, 'turmas': turmas})
