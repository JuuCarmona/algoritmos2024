def binario_recursivo(n):
    if n < 0:
        return "Erro: O número deve ser não negativo."
    elif n == 0:
        return '0'
    elif n == 1:
        return '1'
    else:
        proximo_digito = str(n % 2)
        resto = binario_recursivo(n // 2)
        return resto + proximo_digito

def main():
    numero = int(input("Digite um número decimal não negativo: "))
    if numero < 0:
        print("Erro: O número deve ser não negativo.")
    else:
        resultado_binario = binario_recursivo(numero)
        print(f"A representação é: {resultado_binario}")

main()
