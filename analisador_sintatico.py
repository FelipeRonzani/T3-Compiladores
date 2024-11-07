import ply.yacc as yacc
from analisador_lexico import tokens


tabela_simbolos = {}

# Funções

def p_programa(p):
    '''programa : lista_de_declaracoes'''
    print("Programa analisado com sucesso!")

def p_lista_de_declaracoes(p):
    '''lista_de_declaracoes : lista_de_declaracoes declaracao
                            | declaracao'''

def p_declaracao(p):
    '''declaracao : declaracao_variavel
                  | declaracao_funcao'''

def p_declaracao_variavel(p):
    '''declaracao_variavel : INTEIRO IDENTIFICADOR FIM_DE_LINHA'''
    tabela_simbolos[p[2]] = 'INTEIRO'
    print(f"Variável '{p[2]}' declarada.")

def p_declaracao_funcao(p):
    '''declaracao_funcao : INTEIRO IDENTIFICADOR_DE_FUNCAO PARENTESES_ESQUERDO parametros PARENTESES_DIREITO FIM_DE_LINHA bloco'''
    print(f"Função '{p[2]}' declarada com parâmetros {p[4]}.")

# Bloco de inicio e fim de linha
    
def p_bloco(p):
    '''bloco : INICIO_DE_BLOCO lista_de_comandos FIM_DE_BLOCO FIM_DE_LINHA'''

# Lista de comandos (como atribuições e chamadas de função)
def p_lista_de_comandos(p):
    '''lista_de_comandos : lista_de_comandos comando
                         | comando'''

# Comando de atribuição (exemplo: "X = 10 .")
def p_comando(p):
    '''comando : IDENTIFICADOR IGUALDADE expressao FIM_DE_LINHA'''
    print(f"Comando de atribuição: {p[1]} = {p[3]}")

# Expressão aritmética (exemplo: "10 + 20")
def p_expressao(p):
    '''expressao : expressao MAIS expressao
                 | expressao MENOS expressao
                 | expressao MULTIPLICACAO expressao
                 | expressao DIVISAO expressao
                 | NUMERO
                 | IDENTIFICADOR'''
    p[0] = p[1]

# Parâmetros de função
def p_parametros(p):
    '''parametros : INTEIRO IDENTIFICADOR
                  | INTEIRO IDENTIFICADOR SEPARADOR parametros
                  | empty'''

# Produção vazia para os casos opcionais
def p_empty(p):
    '''empty :'''
    pass

# Tratamento de erros sintáticos
def p_error(p):
    if p:
        print(f"Erro sintático: token inesperado '{p.value}'")
    else:
        print("Erro sintático: final inesperado")

# Função para processar a entrada
def ler_entrada():
    while True:
        print("\nDigite o código ELGOL (escreva 'sair' para encerrar):")
        linhas = []
        while True:
            linha = input()
            if linha.strip().lower() == 'sair':
                break
            linhas.append(linha)
        codigo = "\n".join(linhas)
        parser.parse(codigo)

# Criando o parser
parser = yacc.yacc()

# Função principal
if __name__ == "__main__":
    ler_entrada()
