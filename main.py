from analisador_lexico import lexer
from analisador_sintatico import parser

def executar_analisador_lexico(arquivo):
    print("\n=== Analisador Léxico ===")
    with open(arquivo, 'r') as f:
        codigo = f.read()
    lexer.input(codigo)
    while True:
        token = lexer.token()
        if not token:
            break
        print(token)

def executar_analisador_sintatico(arquivo):
    print("\n=== Analisador Sintático ===")
    with open(arquivo, 'r') as f:
        codigo = f.read()
    resultado = parser.parse(codigo)
    print("Análise Sintática Concluída!")

def main():
    print("Escolha uma opção:")
    print("1 - Analisador Léxico")
    print("2 - Analisador Sintático")
    print("3 - Executar ambos os analisadores")
    opcao = input("Opção: ")

    arquivo = input("Digite o nome do arquivo a ser analisado: ")
    
    if opcao == "1":
        executar_analisador_lexico(arquivo)
    elif opcao == "2":
        executar_analisador_sintatico(arquivo)
    elif opcao == "3":
        executar_analisador_lexico(arquivo)
        executar_analisador_sintatico(arquivo)
    else:
        print("Opção inválida.")

if __name__ == "__main__":
    main()
