from django import forms
from login.models import Aluno, Professor
from .models import Turma, Matricula, Nota

class AlunoForm(forms.ModelForm):
    class Meta:
        model = Aluno
        fields = ['nome', 'data_nascimento', 'email', 'telefone', 'turma']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Personaliza o dropdown de turmas
        self.fields['turma'].queryset = Turma.objects.all()
        self.fields['turma'].label = "Turma"

class TurmaForm(forms.ModelForm):
    class Meta:
        model = Turma
        fields = ['nome', 'ano', 'periodo', 'professor']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['professor'].queryset = Professor.objects.all()
        self.fields['professor'].label = "Professor Responsável"

class NotaForm(forms.ModelForm):
    class Meta:
        model = Nota
        fields = ['nota']

    def __init__(self, *args, **kwargs):
        super(NotaForm, self).__init__(*args, **kwargs)
        # Dynamically add fields for each aluno
        alunos = kwargs.get('data').getlist('nota_')
        for aluno_id in alunos:
            self.fields[f'nota_{aluno_id}'] = forms.DecimalField(max_digits=4, decimal_places=2, min_value=0, max_value=10, required=True)


class MatriculaForm(forms.ModelForm):
    class Meta:
        model = Matricula
        fields = ['aluno', 'turma']
        widgets = {
            'aluno': forms.Select(attrs={'class': 'form-control'}),
            'turma': forms.Select(attrs={'class': 'form-control'}),
        }