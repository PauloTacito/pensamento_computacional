import funcoes

while True:
    print("=" * 70)
    print("            DIÁRIO DE CLASSE ELETRÔNICO - MÓDULO DOCENTE")
    print("=" * 70)

    print("    [A] Verificar aluno cadastrado")
    print("    [B] Listar todos os alunos")
    print("    [C] Listar alunos por turma")
    print("    [D] Listar turmas")
    print("    [E] Iniciar chamada")
    print("    [F] Filtrar alunos")
    print("    [G] Listar datas das aulas")
    print("    [H] Sair")

    print("-" * 70)

    opcao = input("Opção Digitada: ").upper()

    if opcao == "A":
        import cadastro

    elif opcao == "B":
        print("\nTodos os alunos:")

        for aluno in funcoes.listar_alunos():
            print(f"Nome: {aluno['nome']} - Turma: {aluno['turma']}")

    elif opcao == "C":
        turma = input("Digite a turma (A, B ou C): ").upper()

        print(f"\nAlunos da turma {turma}:")

        for aluno in funcoes.listar_alunos_por_turma(turma):
            print(f"Nome: {aluno['nome']} - Turma: {aluno['turma']}")

    elif opcao == "D":
        import turmas

    elif opcao == "E":
        import presenca

    elif opcao == "F":
        import filtrar

    elif opcao == "G":
        import datas

    elif opcao == "H":
        print("Sistema encerrado.")
        break

    else:
        print("Opção inválida!")

    print()