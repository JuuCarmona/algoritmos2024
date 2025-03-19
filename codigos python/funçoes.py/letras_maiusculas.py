def maiusculas(texto):
    texto_corrigido = ""
    maiuscula = True  
    
    for char in texto:
        if maiuscula and char.isalpha():  
            texto_corrigido += char.upper()
            maiuscula = False
        else:
            texto_corrigido += char
            
        if char in ".!?":
            maiuscula = True
    
    return texto_corrigido

def main():
    entrada = input("Digite uma string para corrigir as letras maiúsculas: ")
    resultado = maiusculas(entrada)
    print("String corrigida:", resultado)

if __name__ == "__main__":
    main()
