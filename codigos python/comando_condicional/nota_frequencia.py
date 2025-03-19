#nota para frequencia
nota = input("digite a nota:")
oitava = int(input("digite a oitava da nota:"))

if oitava < 0 or oitava > 8:
    print("não pode ser menor que 0 e maior que 8.")
else:
    if nota == "C":
        frequencia = 261.63
    elif nota == "D":
         frequencia = 293.66
    elif nota == "E":
         frequencia = 329.63
    elif nota == "F":
        frequencia = 349.23
    elif nota == "G":
         frequencia = 392.00
    elif nota == "A":
        frequencia = 440.00
    elif nota == "B":
        frequencia = 493.88
    frequencia_f = frequencia / 2**(4 - oitava)
    print("A frenquência é",frequencia_f)
