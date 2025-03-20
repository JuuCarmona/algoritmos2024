def raiz_quadrada(n, estimativa=1.0):
    if abs(estimativa ** 2 - n) <= 1e-12:
        return estimativa
    else:
        nova_estimativa = (estimativa + n / estimativa) / 2
        return raiz_quadrada(n, nova_estimativa)

def main():
    valores = [25, 49, 81, 100, 144]
    for valor in valores:
        resultado = raiz_quadrada(valor)
        print(f"A raiz quadrada de {valor} é aproximadamente {resultado:.8f}")

main()
