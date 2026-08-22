def prod(a,b):
    if b==1:
        return a
    sum = prod(a,b-1)
    mul = sum + a
    return mul





print(prod(3,5))