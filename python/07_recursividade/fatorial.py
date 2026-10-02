def fatorial(n):
    if n == 1:
        return 1
    else:
        return n * fatorial(n - 1)

numero = 8
print(f"O fatorial é {fatorial(numero)}")
