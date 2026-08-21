alunos = ["Pedro", "Ana", "João", "Maria", "Lucas", "Sofia", "Gabriel", "Beatriz", "Rafael", "Camila"]
letra = "a"

resultado = [aluno for aluno in alunos if aluno.endswith(letra)]

print(resultado)