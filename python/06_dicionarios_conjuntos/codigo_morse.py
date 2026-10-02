def traduzir_para_morse(mensagem):
    
    morse = {
        'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
        'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
        'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
        'Y': '-.--', 'Z': '--..',
        '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....',
        '7': '--...', '8': '---..', '9': '----.',
    }
    
    mensagem_em_morse = ''
    for i in mensagem:
        
        if i.upper() in morse:
            mensagem_em_morse = mensagem_em_morse + morse[i.upper()] + ' '
        elif i == ' ':
            mensagem_em_morse = mensagem_em_morse + ' '
    
    return mensagem_em_morse.strip()  

mensagem = input("Digite a mensagem: ")

mensagem_traduzida = traduzir_para_morse(mensagem)
print("Em código Morse:", mensagem_traduzida)
