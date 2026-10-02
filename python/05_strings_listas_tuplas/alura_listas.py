#lista com numeros de 1 a 10,com 4 nomes, o ano em q nasceu e o ano atual
numeros = list(range(1,11))
print(numeros)

nomes = ["laura","maria", "anna", "carla"]
print(nomes)

ano = [2005,2026]
print(ano)

#lista de quatro strings,com laço de repetiçao.
pais = ['brasil',"eua","portugal","mexico"]
for pais in (pais):
    print(pais)

# lista para somatoria dos numeros impares de 1 a 10, com uso de laço de repetiçao.
impares = 0
for i in range(1,11,2):
    impares = impares + i
    print(impares)

for numeros in range(10,0,-1):
    print(numeros)

#laço de repetiçao pra tabuada, tendo entrada do usuario.
tabuada = int(input("Digite um número para gerar a tabuada dele:"))
for i in range(1,11):
    resultado = tabuada * i
    print(f'{tabuada}*{i}={resultado}')
