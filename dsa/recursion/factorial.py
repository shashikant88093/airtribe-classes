def fact(n):
    if n <=1 :
        return n
    
    top = n
    prod = top * fact(n-1)
    return prod

print(fact(9))