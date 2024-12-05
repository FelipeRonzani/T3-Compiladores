import ply.yacc as yacc
from analisador_lexico import tokens

# Regra inicial
def p_program(p):
    '''program : declaracoes
               | blocos
               | program declaracoes
               | program blocos'''
    print("Programa reconhecido.")

# Declarações gerais (funções ou variáveis)
def p_declaracoes(p):
    '''declaracoes : funcao_declaracao
                   | declaracao'''
    pass

# Declaração de funções
def p_funcao_declaracao(p):
    '''funcao_declaracao : INTEIRO ID LPAREN parametros RPAREN DOT'''
    print(f"Declaração de função reconhecida: {p[2]} com parâmetros {p[4]}")

# Blocos principais
def p_blocos(p):
    '''blocos : INICIO DOT comandos FIM DOT'''
    print("Bloco reconhecido.")

def p_comandos(p):
    '''comandos : comando
                | comandos comando'''
    pass

def p_comando(p):
    '''comando : declaracao
               | atribuicao
               | estrutura_controle
               | funcao_chamada
               | elgio_comando'''
    pass

# Declarações de variáveis
def p_declaracao(p):
    '''declaracao : INTEIRO ID DOT'''
    print(f"Declaração reconhecida: {p[2]}")

# Atribuições
def p_atribuicao(p):
    '''atribuicao : ID ASSIGN expressao DOT'''
    print(f"Atribuição reconhecida: {p[1]} = {p[3]}")

# Estruturas de controle
def p_estrutura_controle(p):
    '''estrutura_controle : ENQUANTO condicao DOT INICIO DOT comandos FIM DOT
                          | SE condicao DOT ENTAO DOT INICIO DOT comandos FIM DOT SENAO DOT INICIO DOT comandos FIM DOT'''
    print("Estrutura de controle reconhecida.")

def p_condicao(p):
    '''condicao : expressao MAIOR expressao
                | expressao MENOR expressao
                | expressao IGUAL expressao
                | expressao DIFERENTE expressao'''
    print("Condição reconhecida.")

# Chamadas de função como fator
def p_funcao_chamada(p):
    '''funcao_chamada : ID LPAREN parametros RPAREN
                      | ID LPAREN RPAREN'''
    if len(p) == 5:
        p[0] = (p[1], p[3])
        print(f"Chamada de função reconhecida: {p[1]} com parâmetros {p[3]}")
    else:
        p[0] = (p[1], None)
        print(f"Chamada de função reconhecida: {p[1]} sem parâmetros")

# Parâmetros em chamadas de função
def p_parametros(p):
    '''parametros : parametro
                  | parametros COMMA parametro'''
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = p[1] + [p[3]]

def p_parametro(p):
    '''parametro : ID
                 | NUM
                 | INTEIRO ID'''
    p[0] = p[1]

# Expressões matemáticas
def p_expressao_binaria(p):
    '''expressao : expressao PLUS termo
                 | expressao MINUS termo'''
    p[0] = (p[1], p[2], p[3])
    print(f"Expressão reconhecida: {p[0]}")

def p_expressao_termo(p):
    '''expressao : termo'''
    p[0] = p[1]

def p_termo_binario(p):
    '''termo : termo MULT fator
             | termo DIV fator'''
    p[0] = (p[1], p[2], p[3])
    print(f"Termo reconhecido: {p[0]}")

def p_termo_fator(p):
    '''termo : fator'''
    p[0] = p[1]

# Fatores incluem chamadas de função
def p_fator(p):
    '''fator : ID
             | NUM
             | ZERO
             | funcao_chamada'''
    p[0] = p[1]
    print(f"Fator reconhecido: {p[0]}")

# Comando para `elgio`
def p_elgio_comando(p):
    '''elgio_comando : ELGIO ASSIGN ID DOT'''
    print(f"Comando elgio reconhecido: {p[3]}")

# Regra para vazio
def p_empty(p):
    'empty :'
    pass

# Erros sintáticos
def p_error(p):
    if p:
        print(f"Erro sintático na linha {p.lineno}: Token inesperado '{p.value}'")
    else:
        print("Erro sintático: Fim inesperado")

parser = yacc.yacc(start='program')