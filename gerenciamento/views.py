from django.shortcuts import render, get_object_or_404, redirect
from login.models import Aluno, Professor
from .models import Turma, Aluno, Matricula, Nota
from .forms import AlunoForm, TurmaForm, MatriculaForm, NotaForm


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
    alunos_com_matriculas = []  # Lista para armazenar os alunos com suas respectivas matrículas

    if request.method == 'POST':
        # Obtém o ID da turma selecionada
        turma_id = request.POST.get('turma')
        turma = get_object_or_404(Turma, id=turma_id)

        # Busca as matrículas dos alunos na turma selecionada
        matriculas = Matricula.objects.filter(turma=turma).select_related('aluno')

        # Itera sobre as matrículas e coleta as notas enviadas
        for matricula in matriculas:
            aluno = matricula.aluno
            # Obtém a nota do aluno com base no ID
            nota = request.POST.get(f'nota_{aluno.id}')

            if nota:
                # Cria a nota associada à matrícula do aluno
                Nota.objects.create(
                    matricula=matricula,
                    nota=nota
                )
        
        return redirect('/')

    # Quando o método não for POST, busca todas as turmas e alunos
    else:        
        turma = Turma.objects.first() 
        # Cria uma lista de alunos com suas respectivas matrículas para passar ao template
        matriculas = Matricula.objects.filter(turma=turma).select_related('aluno')
        alunos_com_matriculas = [(matricula.aluno, matricula) for matricula in matriculas]  

    turmas = Turma.objects.all()  # Carrega todas as turmas para o formulário

    # Renderiza o template e passa os dados necessários
    return render(request, 'gerenciamento/incluir_nota.html', {
        'turmas': turmas,
        'alunos_com_matriculas': alunos_com_matriculas,
        'turma': turma
    })



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
    turmas = Turma.objects.all()  # Carrega todas as turmas para o formulário
    notas = []

    if request.method == 'POST':
        # Recupera a turma selecionada no formulário
        turma_id = request.POST.get('turma')
        turma = get_object_or_404(Turma, id=turma_id)

        # Recupera as notas da turma selecionada
        notas = Nota.objects.filter(matricula__turma=turma).select_related('matricula__aluno')
    else:
        turma = Turma.objects.first()
        # Recupera as notas da turma selecionada
        notas = Nota.objects.filter(matricula__turma=turma).select_related('matricula__aluno')


    return render(request, 'gerenciamento/verificar_nota.html', {
        'turmas': turmas,
        'notas': notas,
    })

'''def verificar_nota(request):
    turmas = Turma.objects.all()  # Recupera todas as turmas
    notas = None  # Inicializa a variável de notas

    if request.method == 'POST':
        # Pega o ID da turma do formulário
        turma_id = request.POST.get('turma_id')
        # Busca a turma com o ID selecionado
        turma = Turma.objects.get(id=turma_id)
        # Recupera as notas dessa turma
        notas = Nota.objects.filter(matricula__turma=turma)

    return render(request, 'gerenciamento/verificar_nota.html', {'turmas': turmas, 'notas': notas})'''


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

def incluir_professor(request):
    if request.method == 'POST':
        # Obtém os dados do formulário
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        especialidade = request.POST.get('especialidade')

        # Cria um novo objeto Professor e salva no banco de dados
        Professor.objects.create(
            nome=nome,
            email=email,
            especialidade=especialidade
        )

        # Redireciona para a mesma página com uma mensagem de sucesso
        return render(request, 'gerenciamento/incluir_professor.html', {'sucesso': True})

    # Para requisições GET, apenas renderiza o formulário vazio
    return render(request, 'gerenciamento/incluir_professor.html')
