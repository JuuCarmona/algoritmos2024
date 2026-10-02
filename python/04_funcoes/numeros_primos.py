def primo(numero):
    if numero <= 1:
        return False
    for i in range (2,numero):
        if numero % i  == 0:        
            return False
    return True

def main():
    numero = int(input("digite o numero:"))

    if primo (numero):
        print(numero,"é primo.")
    else: 
        print(numero, "não é primo.")

if __name__  == "__main__":
    main()
