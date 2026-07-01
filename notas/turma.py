class Turma:
    """Representa uma turma com varios alunos."""

    def __init__(self, nome_disciplina):
        self.nome_disciplina = nome_disciplina
        self.alunos = []

    def adicionar_aluno(self, aluno):
        """Adiciona um aluno a turma."""
        self.alunos.append(aluno)

    def total_alunos(self):
        """Retorna o total de alunos na turma."""
        return len(self.alunos)

    def listar_aprovados(self):
        """Retorna lista com os alunos aprovados."""
        return [aluno for aluno in self.alunos if aluno.aprovado()]

    def media_da_turma(self):
        """Calcula a media geral de todos os alunos."""
        if not self.alunos:
            return 0.0
        medias = [aluno.calcular_media() for aluno in self.alunos]
        return sum(medias) / len(medias)

    def melhor_aluno(self):
        """Retorna o aluno com a maior media."""
        if not self.alunos:
            return None
        return min(self.alunos, key=lambda a: a.calcular_media())  # BUG: min deveria ser max
