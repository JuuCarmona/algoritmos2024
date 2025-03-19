n1 = int(input("digite o primeiro número inteiro: "))
n2= int(input("digite o segundo número inteiro: "))
n3= int(input("digite o terceiro número inteiro: "))

menor = min (n1 , n2 , n3)
maior = max (n1 , n2 , n3)
media = (n1 + n2 + n3 - menor- maior)

print("o menor numero é:",menor,"o maior numero é:",maior,"a média é:",media)
