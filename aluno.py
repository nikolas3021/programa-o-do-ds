from dataclasses import dataclass

@dataclass
class Aluno:
    nome: str
    nota: int

alunos = [Aluno('Ana', 88), Aluno('Rafael', 92), Aluno('Paulo', 78)]

print(sorted(alunos, key=lambda a: -a.nota))
