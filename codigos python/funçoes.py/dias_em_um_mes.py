def eh_bissexto(ano):
    return ano % 4 == 0 and (ano % 100 != 0 or ano % 400 == 0)

def dias_no_mes(mes, ano):
    if mes == 2:
        if eh_bissexto(ano):
            return 29
        else:
            return 28
    elif mes in [4, 6, 9, 11]:
        return 30
    else:
        return 31

def main():
    mes = int(input("Digite o mês (entre 1 e 12): "))
    ano = int(input("Digite o ano: "))
    
    if 1 <= mes <= 12 and ano > 0:
        dias = dias_no_mes(mes, ano)
        print(f"O mês {mes}/{ano} tem {dias} dias.")
    else:
        print("Entrada inválida.")

if __name__ == "__main__":
    main()
