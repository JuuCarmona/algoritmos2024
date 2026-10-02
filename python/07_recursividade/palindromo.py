def eh_palindromo(s):
    
    def verifica_palindromo(s):
       
        s = ''.join(c for c in s if c.isalnum())
        if len(s) <= 1:
            return True
        elif s[0] != s[-1]:
            return False
        else:
            return verifica_palindromo(s[1:-1])

    return verifica_palindromo(s)


string = "saudavel leva duas"
print(f'{eh_palindromo(string)}')
