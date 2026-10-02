centavos = int(input("digite a quantidade de centavos: "))

moedas = [50 , 25 , 10 , 5 , 1]

print("o troco em centavos é:")
print(centavos //50, "moeda(s) de 50 centavo(s)")
centavos %=50
print(centavos //25, "moeda(s) de 25 centavo(s)")
centavos %=25
print (centavos //10, "moeda(s) de 10 centavo(s)")
centavos %=10
print (centavos //5, "moeda(s) de 5 centavo(s)")
centavos %=5
print (centavos //1,"moeda(s) de 1 centavo(s)")
centavos %=1
