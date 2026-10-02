def mdc(a,b):
    if b == 0:
        return a
    else:
        c = a % b
        return mdc(b,c)
    
a = 5
b = 9

print(f"O máximo divisor comum é:{mdc(a,b)}")
