from django.db import models
from login.models import Aluno, Professor

class Turma(models.Model):
    nome = models.CharField(max_length=50)
    ano = models.IntegerField()
    periodo = models.CharField(max_length=20)  # Ex.: Manhã, Tarde, Noite
    professor = models.ForeignKey(Professor, on_delete=models.SET_NULL, null=True)
    def __str__(self):
        return f"{self.nome} - {self.ano} - {self.periodo}"


class Matricula(models.Model):
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE)
    turma = models.ForeignKey(Turma, on_delete=models.CASCADE)
    data_matricula = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"Matrícula: {self.aluno.usuario.username} na turma {self.turma.nome}"

class Nota(models.Model):
    turma = models.ForeignKey(Turma, on_delete=models.CASCADE)
    nota = models.DecimalField(max_digits=4, decimal_places=2)  # Ex.: 7.5, 9.0, etc.
    data_atribuicao = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"Nota de {self.nota} para {self.matricula.aluno.usuario.username} em {self.disciplina.nome}"
