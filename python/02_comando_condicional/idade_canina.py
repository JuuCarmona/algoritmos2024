idade_canina = int(input("digite a idade do seu cão: "))

if idade_canina<0:
    print("o número n pode ser negativo")
elif idade_canina <= 2:
    total = idade_canina*10.5
    print("idade canina:",total)
else:
     total = (idade_canina-2)*4 + (2* 10.5)
     print("idade canina:",total)
