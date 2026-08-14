alunos = ["Pedro", "Ana", "João", "Maria", "Lucas", "Sofia", "Gabriel", "Beatriz", "Rafael", "Camila"]
alnInput = input("Digite o nome do aluno(a): ")

if alnInput in alunos:
    print(f"O aluno(a) {alnInput} está cadastrado(a).")
else:
    print(f"O aluno(a) {alnInput} não está cadastrado(a).")