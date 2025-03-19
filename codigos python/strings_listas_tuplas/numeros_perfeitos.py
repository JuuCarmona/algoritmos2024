def n_perfeito(n):
    soma = 0
    for i in range(1, n):
        if n % i == 0:
            soma = soma + i
    return soma == n

def main():
    for num in range(1, 10001):
        if n_perfeito(num):
            print(num)

if __name__ == "__main__":
    main()
