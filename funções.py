alunos = [
    {"nome": "Ana", "turma": "A"},
    {"nome": "Bruno", "turma": "B"},
    {"nome": "Carlos", "turma": "A"},
    {"nome": "Daniela", "turma": "C"},
    {"nome": "Eduardo", "turma": "B"}
]


def listar_alunos():
    """Retorna a lista de todos os alunos."""
    return alunos


def listar_alunos_por_turma(turma):
    """Retorna os alunos pertencentes à turma informada."""
    return [aluno for aluno in alunos if aluno["turma"] == turma]


# Exemplos de uso
print("Todos os alunos:")
print(listar_alunos())

print("\nAlunos da turma A:")
print(listar_alunos_por_turma("A"))