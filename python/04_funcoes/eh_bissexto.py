def eh_bissexto(ano):
    return ano % 4 == 0 and (ano % 100!= 0 or ano % 400 == 0)
ano = 2024
print(f"{eh_bissexto(ano)}")
