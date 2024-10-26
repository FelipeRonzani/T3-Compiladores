import analisador_lexico
import analisador_sintatico

def menu():
    while True:
        print("\nEscolha o analisador que deseja executar:")
        print("1. Analisador Léxico")
        print("2. Analisador Sintático")
        print("3. Sair\n")

        opcao = input("Opção: ")

        if opcao == '1':
            print("\nExecutando Analisador Léxico...")
            analisador_lexico.ler_entrada()  # Chama a função principal do analisador léxico

        elif opcao == '2':
            print("\nExecutando Analisador Sintático...")
            analisador_sintatico.ler_entrada()  # Chama a função principal do analisador sintático

        elif opcao == '3':
            print("\nSaindo...")
            break

        else:
            print("\nOpção inválida! Tente novamente.")

if __name__ == "__main__":
    menu()
