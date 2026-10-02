# Algoritmos e Lógica de Programação

Mais de 100 exercícios resolvidos em Python e em C enquanto eu aprendia algoritmos e lógica de programação no curso de Ciência da Computação do IFC (Instituto Federal Catarinense), a partir de 2024.

Cada arquivo resolve um problema e roda de forma independente. As pastas de Python estão numeradas em ordem de dificuldade.

## Conteúdo

### Python

| Pasta | Assunto | Exercícios |
| --- | --- | --- |
| [`01_introducao`](python/01_introducao) | Entrada e saída, variáveis, operações aritméticas | 19 |
| [`02_comando_condicional`](python/02_comando_condicional) | `if`, `elif`, `else` | 12 |
| [`03_lacos_de_repeticao`](python/03_lacos_de_repeticao) | `for` e `while` | 21 |
| [`04_funcoes`](python/04_funcoes) | Funções, parâmetros e retorno | 25 |
| [`05_strings_listas_tuplas`](python/05_strings_listas_tuplas) | Strings, listas e tuplas | 16 |
| [`06_dicionarios_conjuntos`](python/06_dicionarios_conjuntos) | Dicionários e conjuntos | 11 |
| [`07_recursividade`](python/07_recursividade) | Funções recursivas | 7 |

### C

| Pasta | Assunto | Exercícios |
| --- | --- | --- |
| [`c`](c) | Fórmula de Bhaskara, médias, vetores, sorteio | 6 |

## Alguns destaques

- [`infix_para_posfix.py`](python/05_strings_listas_tuplas/infix_para_posfix.py): converte uma expressão matemática da notação infixa para a pós-fixada, respeitando a precedência dos operadores.
- [`tokenizacao.py`](python/05_strings_listas_tuplas/tokenizacao.py): separa uma expressão matemática em números, operadores e parênteses.
- [`conversao_base.py`](python/04_funcoes/conversao_base.py): converte números entre quaisquer bases de 2 a 16.
- [`cifra_de_cesar.py`](python/03_lacos_de_repeticao/cifra_de_cesar.py): cifra uma mensagem com deslocamento positivo ou negativo.
- [`codigo_morse.py`](python/06_dicionarios_conjuntos/codigo_morse.py): traduz texto para código Morse com um dicionário.
- [`fibonacci.py`](python/07_recursividade/fibonacci.py) e [`mdc.py`](python/07_recursividade/mdc.py): soluções recursivas.

## Como executar

```bash
git clone https://github.com/JuuCarmona/algoritmos2024.git
cd algoritmos2024
```

Python (versão 3, sem dependências externas):

```bash
python python/05_strings_listas_tuplas/infix_para_posfix.py
```

```text
Digite a expressão infixa: 3 + 4 * 2
Expressão pós-fixada: 3 4 2 * +
```

C (com o GCC):

```bash
gcc c/bhaskara.c -o bhaskara -lm
./bhaskara
```

## Autora

Julia Carmona, estudante de Ciência da Computação no IFC.
[github.com/JuuCarmona](https://github.com/JuuCarmona)
