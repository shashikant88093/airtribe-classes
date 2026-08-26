# how work 1234
# how work 4321

# how work 123321

def PI(n): # print Incresing
    
    if n==0:
        return
    PI(n-1)
    print(n) 


def PD(n): # print Decreasing
    
    if n==0:
        return
    print(n) 
    
    PD(n-1)

def PDI(n): # print Decreasing
    
    if n==0:
        return
    print(n) 
    
    PDI(n-1)
    print(n) 


PI(5)
print("########### PI" )

PD(5)
print("########### PD")
PDI(5)
print("########### PDI")
