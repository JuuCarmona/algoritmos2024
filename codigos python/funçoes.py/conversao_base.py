def base_10(numero, base):
    numero = numero.upper()
    hex_dict = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}
    decimal = 0
    
    for digit in numero:
        decimal = decimal * base + hex_dict[digit]
    return decimal

def base_10_para_base_arbitraria(decimal, base):
    if decimal == 0:
        return '0'
    
    hex_dict = {0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9', 10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}
    resultado = ''
    
    while decimal > 0:
        resto = decimal % base
        resultado = hex_dict[resto] + resultado
        decimal //= base
    return resultado

def main():
    entrada = int(input("Digite a base do número de entrada entre 2 e 16: "))
    saida = int(input("Digite a base para converter o número entre 2 e 16: "))
    numero = input(f"Digite o número na base {entrada}: ")
    
    if 2 <= entrada <= 16 and 2 <= saida <= 16:
        if all(digito.upper() in "0123456789ABCDEF" for digito in numero) and base_10(numero, entrada) >= 0:
            decimal = base_10(numero,entrada)
            resultado = base_10_para_base_arbitraria(decimal, saida)
            print(f"O número {numero} na base {entrada} é equivalente a {resultado} na base {saida}.")
        else:
            print("Número inválido.")
    else:
        print("Bases inválidas")

if __name__ == "__main__":
    main()
