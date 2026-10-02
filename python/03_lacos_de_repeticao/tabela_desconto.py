preços = [4.95, 9.95, 14.95, 19.95, 24.95]
desconto = 0.6  

print("Preço Original , Desconto , Preço com Desconto")
for preço in preços:
    desconto = preço * (1 - desconto)
    print(f"R$ {preço:.2f} , R$ {desconto:.2f}")
