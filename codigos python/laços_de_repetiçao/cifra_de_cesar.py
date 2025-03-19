mensagem = input("Digite a mensagem: ")
deslocamento = int(input("Digite o deslocamento (pode ser negativo): "))

mensagem_cifrada = ''
for caractere in mensagem:
    if 'a' <= caractere <= 'z': 
        novo_codigo = (ord(caractere) - ord('a') + deslocamento) % 26 + ord('a')
        mensagem_cifrada = mensagem_cifrada + chr(novo_codigo)
    elif 'A' <= caractere <= 'Z': 
        novo_codigo = (ord(caractere) - ord('A') + deslocamento) % 26 + ord('A')
        mensagem_cifrada = mensagem_cifrada + chr(novo_codigo)
    else:
        mensagem_cifrada = mensagem_cifrada + caractere  

print("Mensagem cifrada:", mensagem_cifrada)
