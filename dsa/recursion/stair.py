

def stair(n):
    
    if n <=2:
        return n
    
    l1 = stair(n-1)
    l2 = stair(n-2)
    way = l1 + l2
    return way


stair(9)