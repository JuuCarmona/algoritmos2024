def encaixa(a, b):
    def conta_digito(num):
        conta = 0
        while num > 0:
            conta = conta + 1
            num = num // 10
        return conta
    
    digitos_b = conta_digito(b)
    
    digitos_a = a % (10 ** digitos_b)
    
    if digitos_a == b:
        return True
    else:
        return False

a = 123456
b = 456
print(encaixa(a,b))
