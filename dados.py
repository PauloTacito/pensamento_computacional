alunos = []
turmas = []
aulas = []
presencas = []


while True:

    print("\n==============================")
    print("     CONTROLE DE PRESENCAS")
    print("==============================")
    print("1 - Cadastrar aluno")
    print("2 - Listar alunos")
    print("3 - Cadastrar turma")
    print("4 - Listar turmas")
    print("5 - Cadastrar aula")
    print("6 - Listar aulas")
    print("7 - Registrar presenca")
    print("8 - Listar presencas")
    print("0 - Sair")
    print("==============================")

    opcao = input("Digite uma opcao: ")


    # =========================
    # CADASTRAR ALUNO
    # =========================

    if opcao == "1":

        print("\n===== CADASTRAR ALUNO =====")

        matricula = input("Digite a matricula: ")
        nome = input("Digite o nome: ")
        email = input("Digite o email: ")

        aluno = {
            "matricula": matricula,
            "nome": nome,
            "email": email
        }

        alunos.append(aluno)

        print("\nAluno cadastrado com sucesso!")


    # =========================
    # LISTAR ALUNOS
    # =========================

    elif opcao == "2":

        print("\n===== LISTA DE ALUNOS =====")

        if len(alunos) == 0:

            print("Nenhum aluno cadastrado.")

        else:

            for aluno in alunos:

                print("Matricula:", aluno["matricula"])
                print("Nome:", aluno["nome"])
                print("Email:", aluno["email"])
                print("------------------------")


    # =========================
    # CADASTRAR TURMA
    # =========================

    elif opcao == "3":

        print("\n===== CADASTRAR TURMA =====")

        codigo = input("Digite o codigo da turma: ")
        disciplina = input("Digite a disciplina: ")
        carga = input("Digite a carga horaria: ")

        turma = {
            "codigo": codigo,
            "disciplina": disciplina,
            "carga": carga
        }

        turmas.append(turma)

        print("\nTurma cadastrada com sucesso!")


    # =========================
    # LISTAR TURMAS
    # =========================

    elif opcao == "4":

        print("\n===== LISTA DE TURMAS =====")

        if len(turmas) == 0:

            print("Nenhuma turma cadastrada.")

        else:

            for turma in turmas:

                print("Codigo:", turma["codigo"])
                print("Disciplina:", turma["disciplina"])
                print("Carga horaria:", turma["carga"])
                print("------------------------")


    # =========================
    # CADASTRAR AULA
    # =========================

    elif opcao == "5":

        print("\n===== CADASTRAR AULA =====")

        codigo = input("Digite o codigo da aula: ")
        disciplina = input("Digite a disciplina: ")
        identificacao = input("Digite a identificacao: ")

        aula = {
            "codigo": codigo,
            "disciplina": disciplina,
            "identificacao": identificacao
        }

        aulas.append(aula)

        print("\nAula cadastrada com sucesso!")


    # =========================
    # LISTAR AULAS
    # =========================

    elif opcao == "6":

        print("\n===== LISTA DE AULAS =====")

        if len(aulas) == 0:

            print("Nenhuma aula cadastrada.")

        else:

            for aula in aulas:

                print("Codigo:", aula["codigo"])
                print("Disciplina:", aula["disciplina"])
                print("Identificacao:", aula["identificacao"])
                print("------------------------")


    # =========================
    # REGISTRAR PRESENCA
    # =========================

    elif opcao == "7":

        print("\n===== REGISTRAR PRESENCA =====")

        matricula = input("Digite a matricula do aluno: ")
        codigo_aula = input("Digite o codigo da aula: ")
        presente = input("O aluno esta presente? (S/N): ")

        if presente == "S" or presente == "s":

            situacao = "Presente"

        else:

            situacao = "Falta"

        presenca = {
            "matricula": matricula,
            "codigo_aula": codigo_aula,
            "situacao": situacao
        }

        presencas.append(presenca)

        print("\nPresenca registrada com sucesso!")


    # =========================
    # LISTAR PRESENCAS
    # =========================

    elif opcao == "8":

        print("\n===== LISTA DE PRESENCAS =====")

        if len(presencas) == 0:

            print("Nenhuma presenca registrada.")

        else:

            for presenca in presencas:

                print("Matricula:", presenca["matricula"])
                print("Codigo da aula:", presenca["codigo_aula"])
                print("Situacao:", presenca["situacao"])
                print("------------------------")


    # =========================
    # SAIR PELO MENU
    # =========================

    elif opcao == "0":

        print("\nPrograma encerrado!")
        break


    # =========================
    # OPCAO INVALIDA
    # =========================

    else:

        print("\nOpcao invalida!")


    # =========================
    # VOLTAR AO MENU OU SAIR
    # =========================

    voltar = input("\nDeseja voltar ao menu? (S/N): ")

    if voltar == "S" or voltar == "s":

        print("\nVoltando ao menu...")

    else:

        print("\nPrograma encerrado!")
        break