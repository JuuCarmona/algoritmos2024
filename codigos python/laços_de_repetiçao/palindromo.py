palavra = input("Digite uma palavra: ")

palavra_invertida = ''
for letra in palavra:
    palavra_invertida = letra + palavra_invertida

if palavra == palavra_invertida:
    print(f'A palavra "{palavra}" é um palíndromo.')
else:
    print(f'A palavra "{palavra}" não é um palíndromo.')
