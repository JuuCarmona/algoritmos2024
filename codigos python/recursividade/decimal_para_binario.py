def bininterativo(q):
    if q == 0:
        return "0"
    else:
        resultado = ""
        while q > 0:
            resto = q % 2
            resultado = str(resto) + resultado
            q = q // 2
        return resultado
    
numero = 8
resultado_final = bininterativo(numero)

print(f"A representação binária é:{bininterativo(numero)}")
