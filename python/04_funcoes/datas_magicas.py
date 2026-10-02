def data_magica(dia, mes, ano):
    digitos_ano = ano % 100
    return dia * mes == digitos_ano

def main():
    for ano in range(1900, 2000):
        for mes in range(1, 13):
            for dia in range(1, 32):
                if dia * mes == ano % 100:
                    print(f"{dia}/{mes}/{ano} é uma data mágica.")

if __name__ == "__main__":
    main()
