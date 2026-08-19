def verificar_presenca():
    alunos = [
        "Marcos",
        "João",
        "Paulo",
        "Jonata",
        "Ana"
    ]

    presentes = []
    ausentes = []

    for aluno in alunos:
        resposta = input("O aluno " + aluno + " está presente? (S/N): ")

        if resposta == "S" or resposta == "s":
            presentes.append(aluno)
        else:
            ausentes.append(aluno)

    print("\nAlunos presentes:")
    print(presentes)

    print("\nAlunos ausentes:")
    print(ausentes)


verificar_presenca()