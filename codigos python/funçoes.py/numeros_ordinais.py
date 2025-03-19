def numero_ordinal(numero):
    ordinais = ["primeiro", "segundo", "terceiro", "quarto", "quinto", "sexto", "sétimo", "oitavo", "nono", "décimo", "décimo primeiro", "décimo segundo"]
    
    if 1 <= numero <= 12:
        return ordinais[numero - 1]
    else:
        return ""

def main():
    for i in range(1, 13):
        print(f"{i}: {numero_ordinal(i)}")

if __name__ == "__main__":
    main()
