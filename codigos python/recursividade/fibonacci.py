def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


numero = 7
print(f"O resultado da sequência de Fibonacci é {fibonacci(numero)}")
