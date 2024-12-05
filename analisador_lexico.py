import ply.lex as lex

# Lista de tokens
tokens = [
    'ID', 'NUM', 'PLUS', 'MINUS', 'MULT', 'DIV', 'ASSIGN', 'DOT',
    'MAIOR', 'MENOR', 'IGUAL', 'DIFERENTE', 'LPAREN', 'RPAREN', 'COMMA'
]

# Palavras reservadas
reserved = {
    'inteiro': 'INTEIRO',
    'inicio': 'INICIO',
    'fim': 'FIM',
    'zero': 'ZERO',
    'enquanto': 'ENQUANTO',
    'se': 'SE',
    'entao': 'ENTAO',
    'senao': 'SENAO',
    'elgio': 'ELGIO'
}

# Adiciona tokens das palavras reservadas
tokens += list(reserved.values())

# Expressões regulares para tokens simples
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_COMMA = r','
t_PLUS = r'\+'
t_MINUS = r'-'
t_MULT = r'x'
t_DIV = r'/'
t_ASSIGN = r'='
t_DOT = r'\.'
t_MAIOR = r'maior'
t_MENOR = r'menor'
t_IGUAL = r'igual'
t_DIFERENTE = r'diferente'

# Ignorar espaços e tabulações
t_ignore = ' \t'

# Identificadores e palavras reservadas
def t_ID(t):
    r'[a-wy-zA-WY-Z_][a-zA-Z0-9_]*'  # Exclui 'x' como identificador válido
    t.type = reserved.get(t.value, 'ID')  # Verifica palavras reservadas
    return t

# Números
def t_NUM(t):
    r'\d+'
    t.value = int(t.value)
    return t

# Comentários
def t_comment(t):
    r'\#.*'
    pass

# Operador inválido
def t_INVALID_OPERATOR(t):
    r'\*'
    print(f"Erro léxico: Operador inválido '*' encontrado na linha {t.lineno}")
    t.lexer.skip(1)

# Nova linha para controle de erros
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# Caracteres inválidos
def t_error(t):
    print(f"Erro léxico na linha {t.lineno}: {t.value[0]}")
    t.lexer.skip(1)

# Construção do analisador léxico
lexer = lex.lex()
