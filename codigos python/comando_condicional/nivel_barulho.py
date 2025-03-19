nivel = float(input("digite o nivel de volume em décibéis: "))
if 40 <= nivel <= 130:
    if nivel == 40:
        print("barulho da sala silenciosa.")
    elif nivel == 70 :
        print("barulho do despertador.") 
    elif nivel == 106 :
        print("barulho do cortador de grama.")
    elif nivel == 130 :
         print("barulho de britadeira.")
    elif nivel >= 40 or nivel <= 70 :
        print("o barulho esta entre o barulho da sala silenciosa e do despertador.")
    elif nivel >= 40 or nivel <= 106 :
        print("o barulho esta entre a sala silenciosa e o cortador de grama.")
    elif nivel >= 40 or nivel <= 130 :
        print("o barulho esta entre a sala silenciosa e a britadeira.") 
    elif nivel >= 70 or nivel <= 106 :
        print("o barulho esta entre o despertador e o cortador de grama.")
    elif nivel >= 70 or nivel <= 130 :
        print("o barulho esta entre o despertador e a britadeira.")
    elif nivel >= 106 or nivel <= 130 :
        print("o barulho esta entre o cortador de grama e a britadeira")
else:
    print("erro!!")
