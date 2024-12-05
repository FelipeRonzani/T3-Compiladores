## Continuação do T1 e T2
#### Feito utilizando PLY. O objetivo deste trabalho é desenvolver um programa capaz de interpretar a linguagem de programação Elgol, neste momento o programa é capaz de gerar uma lista de tokens e uma tabela de símbolos, salvando ambos em arquivos separados para melhor visualização, baseado na entrada que pode ser realizada manualmente ou através de um arquivo com o código através de um menu interativo no terminal.
## Grupo
#### Cleber Trindade, Felipe Ronzani e Gabriel Uchaki.
## Instruções de uso
#### Para poder executar o projeto é preciso instalar o PLY, pode ser utilizado o seguinte comando para instalar via pip: 
#### pip install ply
#### Execute main.py e siga as instruções do menu interativo.
#### Utilize um arquivo txt(ou utilize o entrada.txt) como entrada(insira o path até o arquivo, não esqueça da extensão do arquivo) ou manualmente digite as linhas de código.
#### Utilize as opções do menu interativo para salvar a lista de tokens ou a tabela de símbolos em seus respectivos arquivos.
## Observações
### Erros Críticos:
### Detecção de Tokens Inválidos:
#### Tokens como * e ; são identificados corretamente como inválidos no analisador léxico. No entanto: Esses tokens geram erros que interrompem o fluxo da análise. Não há continuidade clara para tratar o restante do código após esses erros.
### Problemas Sintáticos em Estruturas de Controle:
#### No arquivo exemplo5.txt, o token diferente não foi reconhecido como parte das estruturas de controle, indicando uma lacuna na gramática sintática para comandos como enquanto e se.
### Tokens Extra ou Erros de Codificação:
#### Erros como Ã e ¡ nos arquivos de exemplo (exemplo2.txt) indicam problemas de codificação (provavelmente UTF-8 mal interpretado ou símbolos fora do escopo da linguagem). Esses erros não são recuperados corretamente, prejudicando a análise.
### Erros em Atribuições e Declarações:
#### O arquivo exemplo4.txt apresentou erros em atribuições como Variaval = Teste + Nada, onde o token Nada não estava definido, mas foi aceito como identificador válido.
### Erros em Atribuições e Declarações:
#### O arquivo exemplo4.txt apresentou erros em atribuições como Variaval = Teste + Nada, onde o token Nada não estava definido, mas foi aceito como identificador válido.
### Falta de Mensagens Detalhadas em Alguns Erros:
#### No analisador sintático, os erros sintáticos carecem de mensagens que expliquem por que um token específico foi inesperado, dificultando o rastreamento do problema.
### Acertos
### Reconhecimento Léxico:
###A maioria dos tokens válidos foi corretamente identificada, incluindo identificadores, números, operadores (x, +, -, /) e palavras reservadas (inteiro, inicio, fim, etc.).
### Estruturas Bem Reconhecidas:
###Declarações de variáveis e funções foram corretamente reconhecidas, como _Fazalgo e _Fazalgo2, com seus respectivos parâmetros.
### Análise de Expressões Matemáticas:
####Expressões como Variavel + 3 - 5 x 2 / 2 + Teste foram reconhecidas corretamente e estruturadas no analisador sintático.
###Mensagens de Reconhecimento:
### Mensagens como "Declaração reconhecida", "Atribuição reconhecida" e "Chamada de função reconhecida" fornecem uma visão clara do que foi processado corretamente.
