def diferenca_simetrica(M, N):
    
    diferença = []
    for num in M:
        if num not in N:
            diferença.append(num)
    for num in N:
        if num not in M:
            diferença.append(num)
   
    diferença.sort()
    return diferença

M = [2, 4, 5, 9]
N = [2, 4, 11, 12]
print(diferenca_simetrica(M, N))  
