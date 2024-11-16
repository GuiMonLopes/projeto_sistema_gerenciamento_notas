from django.db import models
from login.models import Aluno, Professor

class Turma(models.Model):
    nome = models.CharField(max_length=55)
    ano = models.IntegerField()  # Ano da turma
    periodo = models.CharField(max_length=20)  # Ex.: Manhã, Tarde, Noite
    professor = models.ForeignKey(Professor, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.nome} - {self.ano} - {self.periodo}"


class Matricula(models.Model):
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE, related_name='matriculas')
    turma = models.ForeignKey(Turma, on_delete=models.CASCADE, related_name='matriculas')
    data_matricula = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"Matrícula: {self.aluno.nome} na turma {self.turma.nome}"

class Nota(models.Model):
    matricula = models.ForeignKey(Matricula, on_delete=models.CASCADE, related_name='notas')
    nota = models.DecimalField(max_digits=4, decimal_places=2, verbose_name="Nota do Aluno")  # Ex.: 7.5, 9.0, etc.
    data_atribuicao = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"Nota: {self.nota} - Aluno: {self.matricula.aluno.nome} - Turma: {self.matricula.turma.nome}"
