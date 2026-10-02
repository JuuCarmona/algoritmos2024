import random

def senha():
    comprimento = random.randint(7, 10)
    senha_aleatória = ""

    for i in range(comprimento):
        senha_aleatória = senha_aleatória + chr(random.randint(33,126))
        return senha_aleatória
    
def main():
    senha_final=senha()
    print("A senha é:", senha_final)

if __name__ == "__main__":
    main()
