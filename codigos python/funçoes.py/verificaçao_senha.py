def letra_maiuscula(caractere):
    return "A" <= caractere <= "Z"

def letra_minuscula(caractere):
    return "a" <= caractere <= "z"

def tem_numero(caractere):
    return "0" <= caractere <= "9"

def validar_senha(senha):
    letra_maiuscula_ = False
    letra_minuscula_ = False
    tem_numero_ = False
    
    for caractere in senha:
        if letra_maiuscula(caractere):
            letra_maiuscula_ = True
        elif letra_minuscula(caractere):
            letra_minuscula_ = True
        elif tem_numero(caractere):
            tem_numero_ = True
    
    return len(senha) >= 8 and letra_maiuscula_ and letra_minuscula_ and tem_numero_

def main():
    senha = input("Digite a senha: ")
    if validar_senha(senha):
        print("Senha válida!")
    else:
        print("Senha inválida!")

if __name__ == "__main__":
    main()
