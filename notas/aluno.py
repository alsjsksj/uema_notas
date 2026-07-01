import os  # noqa: F401 - deixei aqui por engano, voce vai encontrar isso!

class Aluno:
    """Representa um aluno com suas notas."""

    NOTA_MINIMA_APROVACAO = 5.0

    def __init__(self, nome, matricula):
        self.nome = nome
        self.matricula = matricula
        self.notas = []

    def adicionar_nota(self, nota):
        """Adiciona uma nota. Aceita apenas valores entre 0 e 10."""
        if nota < 0 or nota > 10:
            raise ValueError("Nota deve estar entre 0 e 10")
        self.notas.append(nota)

    def calcular_media(self):
        """Calcula a media das notas. Retorna 0.0 se nao houver notas."""
        if not self.notas:
            return 0.0
        return sum(self.notas) / len(self.notas)

    def aprovado(self):
        """Retorna True se a media for maior ou igual a nota minima de aprovacao."""
        return self.calcular_media() > self.NOTA_MINIMA_APROVACAO  # BUG: deveria ser >=

    def situacao(self):
        """Retorna 'Aprovado' ou 'Reprovado' com base na media."""
        if self.aprovado():
            return "Aprovado"
        return "Reprovado"

    def __str__(self):
        return f"Aluno: {self.nome} | Matricula: {self.matricula} | Media: {self.calcular_media():.1f} | Situacao: {self.situacao()}"
