import funcoes

print("Todos os alunos:")

for aluno in funcoes.listar_alunos():
    print(f"Nome: {aluno['nome']} - Turma: {aluno['turma']}")


print("\nAlunos da turma A:")

for aluno in funcoes.listar_alunos_por_turma("A"):
    print(f"Nome: {aluno['nome']} - Turma: {aluno['turma']}")


print("\nAlunos da turma B:")

for aluno in funcoes.listar_alunos_por_turma("B"):
    print(f"Nome: {aluno['nome']} - Turma: {aluno['turma']}")


print("\nAlunos da turma C:")

for aluno in funcoes.listar_alunos_por_turma("C"):
    print(f"Nome: {aluno['nome']} - Turma: {aluno['turma']}")