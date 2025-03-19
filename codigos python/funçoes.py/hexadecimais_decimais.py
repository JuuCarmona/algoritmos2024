def hex2int(hexadecimal):
    hexadecimal = hexadecimal.upper()
    hex_dict = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}
    decimal = 0
    
    for digit in hexadecimal:
        decimal = decimal * 16 + hex_dict[digit]
    
    return decimal

def int2hex(decimal):
    if decimal < 0 or decimal > 15:
        return "Número fora do intervalo [0, 15]"
    
    hex_dict = {0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9', 10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}
    
    return hex_dict[decimal]

def main():
    print(hex2int('A'))  
    print(hex2int('1A'))  
    print(hex2int('FF'))  
    print(hex2int('2F'))  
    
    print(int2hex(10))  
    print(int2hex(15))  
    print(int2hex(7))   

if __name__ == "__main__":
    main()
