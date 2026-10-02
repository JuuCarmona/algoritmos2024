def tarifa(distancia):
    valor_inicial = 4.00
    taxa = 0.25
    metros = distancia * 1000
    extra = metros / 140 * 0.14

    total = valor_inicial + taxa * (distancia + extra)
    return total

def main():
    distancia = float(input("digite a distância em quilômetros:"))
    total = tarifa(distancia)
    
    print("O valor total da corrida é R$:", total)
main()
