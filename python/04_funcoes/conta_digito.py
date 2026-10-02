def conta_digitos(n, d):
    if not 0 < d <= 9:
        print("O dígito deve ser um número entre 1 e 9.")
    
    conta = 0
    while n > 0:
        if n % 10 == d:
            conta = conta + 1
        n= n // 10
    
    return conta
numero = 15042024
digito = 5
print(f"O dígito {digito} aparece {conta_digitos(numero, digito)}vezes.")
