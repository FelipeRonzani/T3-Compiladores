import ply.lex as lex
import os
import sys

# Adicionado para suprimir os avisos de duplicação de identificação 
# das palavras reservadas e manter o terminal mais limpo.
sys.stderr = open(os.devnull, 'w')

# Palavras reservadas
reserved = {
    'elgio': 'RETORNO',
    'inteiro': 'INTEIRO',
    'zero': 'ZERO',
    'comp': 'COMPLEMENTO',
    'enquanto': 'CONDICIONAL',
    'se': 'CONDICIONAL',
    'entao': 'CONDICIONAL',
    'senao': 'CONDICIONAL',
    'inicio': 'INICIO_DE_BLOCO',
    'fim': 'FIM_DE_BLOCO',
    'maior': 'RELACIONAL',
    'menor': 'RELACIONAL',
    'igual': 'RELACIONAL',
    'diferente': 'RELACIONAL'
}

# Tokens
tokens = [
    'IDENTIFICADOR',        # Identificadores
    'IDENTIFICADOR_DE_FUNCAO',   # Identificadores de funções
    'NUMERO',    # Números
    'COMENTARIO',# Comentário
    'MAIS',      # +
    'MENOS',     # -
    'MULTIPLICACAO',      # x
    'DIVISAO',       # /
    'IGUALDADE', # =
    'PARENTESES_ESQUERDO',    # (
    'PARENTESES_DIREITO',    # )
    'FIM_DE_LINHA',     # .
    'SEPARADOR',   # ,
    'ERRO'  # Token para erro léxico
] 

# Adiciona as palavras reservadas como um conjunto de tokens
tokens += list(reserved.values())

# Regras para expressões regulares dos tokens
t_MAIS    = r'\+'
t_MENOS   = r'-'
t_MULTIPLICACAO    = r'x'
t_DIVISAO     = r'/'
t_IGUALDADE = r'='
t_PARENTESES_ESQUERDO  = r'\('
t_PARENTESES_DIREITO  = r'\)'
t_FIM_DE_LINHA   = r'\.'
t_SEPARADOR = r','

# Expressão regular para comentários (iniciam com # e vão até o fim da linha)
def t_COMENTARIO(t):
    r'\#.*'
    pass  # Ignora comentários

# Expressão regular para palavras reservadas e identificadores
def t_IDENTIFICADOR(t):
    r'[A-Za-z][A-Za-z]*'
    if t.value in reserved:
        t.type = reserved[t.value]  # Se a palavra for reservada, adiciona o tipo com base no valor do dicionário
        symbol_table[t.value] = reserved[t.value]  # Armazena a palavra reservada na tabela de símbolos
    elif t.value[0].isupper() and len(t.value) >= 3:
        t.type = 'IDENTIFICADOR'  # Verifica se o identificador é válido
        symbol_table[t.value] = 'IDENTIFICADOR'  # Adiciona à tabela de símbolos
    else:
        # Identificador inválido, registra como erro
        t.type = 'ERRO'
        t.value = 'identificador invalido'
        print(f"\nErro léxico: um identificador inválido.")
    return t

# Expressão regular para identificadores de função
def t_IDENTIFICADOR_DE_FUNCAO(t):
    r'\_[A-Z][A-Za-z]*'  # Identificador de função começa com _ seguido de letra maiúscula
    if len(t.value) >= 4:  # Verifica se tem pelo menos 4 caracteres
        symbol_table[t.value] = 'IDENTIFICADOR DE FUNCAO'  # Adiciona à tabela de símbolos
        return t
    else:
        # Identificador de função inválido, registra como erro
        t.type = 'ERRO'
        t.value = 'identificador de funcao invalido'
        print(f"\nErro léxico: um identificador de função inválido.")
        return t

# Expressão regular para números inteiros
def t_NUMERO(t):
    r'[1-9]\d*'  # Apenas números inteiros que não começam com 0
    if t.value.isdigit():  # Verifica se o valor é um número
        symbol_table[t.value] = 'NUMERO'  # Adiciona à tabela de símbolos
    else:
        # Se o número não for válido, registra como erro
        print(f"\nErro léxico: um número inválido.")
        t.type = 'ERRO'
        t.value = 'numero invalido'
        return t
    return t

# Ignora espaços em branco e tabulações
t_ignore = ' \t\n'

# Tratamento de erros
def t_error(t):
    t.type = 'ERRO'
    t.value = f"{t.value[0]} (caractere invalido)"
    tokens_list.append(t)  # Adiciona o token de erro à lista de tokens
    t.lexer.skip(1)  # Ignora o caractere inválido

# Cria o lexer
lexer = lex.lex()

# Lista para armazenar os tokens
tokens_list = []

# Tabela de símbolos (dicionário para armazenar identificadores, funções e números)
symbol_table = {}

# Função para processar a entrada e gerar tokens e tabela de símbolos
def processa_entrada(input_data):
    lexer.input(input_data)
    while True:
        tok = lexer.token()
        if not tok:
            break
        tokens_list.append(tok)  # Adiciona cada token à lista de tokens

# Função para salvar a tabela de símbolos em um arquivo
def salvar_tabela_de_simbolos():
    with open("tabela_de_simbolos.txt", 'w') as f:
        f.write("Tabela de Simbolos:\n")
        for simbolo, tipo in symbol_table.items():
            f.write(f"{simbolo}: {tipo}\n")

# Função para salvar a lista de tokens em um arquivo
def salvar_lista_de_tokens():
    with open("lista_de_tokens.txt", 'w') as f:
        f.write("Lista de Tokens:\n")
        for token in tokens_list:
            f.write(f"{token}\n")

# Função para ler arquivo ou entrada manualmente
def ler_entrada():
    while True:
        print("\nEscolha uma opção:")
        print("1. Inserir código manualmente")
        print("2. Carregar código de um arquivo")
        print("3. Salvar tabela de símbolos")
        print("4. Salvar lista de tokens")
        print("5. Sair\n")

        opcao = input("Opção: ")

        if opcao == '1':
            print("Digite seu código (escreva 'sair' para parar):")
            linhas = []
            while True:
                linha = input()
                if linha.strip().lower() == 'sair':
                    break
                linhas.append(linha)
            codigo = "\n".join(linhas)
            processa_entrada(codigo)

        elif opcao == '2':
            nome_arquivo = input("\nInsira o caminho do arquivo (com extensão): ")
            try:
                with open(nome_arquivo, 'r') as arquivo:
                    codigo = arquivo.read()
                processa_entrada(codigo)
            except FileNotFoundError:
                print("Arquivo não encontrado!")

        elif opcao == '3':
            salvar_tabela_de_simbolos()

        elif opcao == '4':
            salvar_lista_de_tokens()

        elif opcao == '5':
            print("Saindo...")
            break

        else:
            print("Opção inválida! Tente novamente.")

# Função Principal
if __name__ == "__main__":
    ler_entrada()
