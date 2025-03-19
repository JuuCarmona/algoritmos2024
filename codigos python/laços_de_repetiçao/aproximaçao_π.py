num_aproximacoes = 15

aprox_pi = 3.0
denominador = 2
sinal = 1

print("Aproximações de pi:")
for pi in range(num_aproximacoes):
    print(aprox_pi)
    
    termo = 4 / (denominador * (denominador + 1) * (denominador + 2))
    aprox_pi = aprox_pi + sinal * termo
    
    denominador = denominador + 2
    sinal = sinal * -1
