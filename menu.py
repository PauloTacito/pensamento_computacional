import dados
import cadastro
import datas
import filtrar
import funcoes
import presenca
import turmas


def exibir_menu():
    while True:
        print("\n" + "=" * 70)
        print("             DIÁRIO DE CLASSE ELETRÔNICO")
        print("=" * 70)
        print("[A] Cadastrar aluno")
        print("[B] Listar alunos")
        print("[C] Listar turmas")
        print("[D] Iniciar chamada")
        print("[E] Consultar presenças")
        print("[F] Calcular frequência")
        print("[G] Filtrar alunos")
        print("[H] Listar datas das aulas")
        print("[I] Cadastrar turma")
        print("[J] Listar aulas/disciplinas")
        print("[K] Verificar aluno")
        print("[L] Abonar falta")
        print("[M] Sair")
        print("-" * 70)

        opcao = input("Opção digitada: ").strip().upper()

        if opcao == "A":
            cadastro.cadastrar_aluno()

        elif opcao == "B":
            if not dados.alunos:
                print("NENHUM ALUNO CADASTRADO!")
            else:
                print("\nAlunos cadastrados:")
                for aluno in funcoes.listar_alunos():
                    print("-", aluno)

        elif opcao == "C":
            if not dados.turmas:
                print("NENHUMA TURMA CADASTRADA!")
            else:
                turmas.listar_turmas()

        elif opcao == "D":
            presenca.verificar_presenca()

        elif opcao == "E":
            presenca.mostrar_presencas()

        elif opcao == "F":
            presenca.calcular_frequencia()

        elif opcao == "G":
            filtrar.mostrar_filtro()

        elif opcao == "H":
            datas.listar_datas()

        elif opcao == "I":
            turmas.cadastrar_turma()

        elif opcao == "J":
            print("\nAulas/disciplinas:")
            for aula in funcoes.listar_aulas():
                print("-", aula)

        elif opcao == "K":
            cadastro.verificar_aluno()

        elif opcao == "L":
            nome = input("Digite o nome do aluno: ").strip()
            presenca.abonar_falta(nome)

        elif opcao == "M":
            print("Sistema encerrado.")
            break

        else:
            print("OPÇÃO INVÁLIDA!")


if __name__ == "__main__":
    exibir_menu()
