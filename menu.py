from cadastro import cadastrar, listar_cadastros
from dados import alunos
from datas import listar_datas
from filtrar import executar_filtro
from presenca import verificar_presenca, listar_presencas, calcular_frequencia
from turmas import listar_turmas


def mostrar_menu():
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
    print("[I] Sair")
    print("-" * 70)


def executar_menu():
    while True:
        mostrar_menu()
        opcao = input("Opção digitada: ").strip().upper()

        if opcao == "A":
            cadastrar()

        elif opcao == "B":
            listar_cadastros()

        elif opcao == "C":
            print("\n--- TURMAS ---")
            for turma in listar_turmas():
                print(
                    f"{turma['codigo_turma']} - {turma['disciplina']} "
                    f"- {turma['carga_horaria']} horas"
                )

        elif opcao == "D":
            verificar_presenca()

        elif opcao == "E":
            listar_presencas()

        elif opcao == "F":
            calcular_frequencia()

        elif opcao == "G":
            executar_filtro()

        elif opcao == "H":
            print("\n--- DATAS DAS AULAS ---")
            for numero, data in listar_datas().items():
                print(f"Aula {numero:02d} - {data}")

        elif opcao == "I":
            print("Sistema encerrado.")
            break

        else:
            print("OPÇÃO INVÁLIDA!")


if __name__ == "__main__":
    executar_menu()
