
# single loop
n = 10
for i in range(1, n+1):
    print(i)

# time complixity O(N)

#  Nested Loop

for i in range(1,n+1):
    for j in range(1,n+1):
        print(i,j)

#  time complixity O(N^2)

m =100
# Different bounds 

for i in range(1, n+1):
    for j in range(1 , m+1):
        print(i,j)

#  time complixity O(N*M)

for i in range (1 ,10):
    for j in range(1, n):
        print(i,j)

#  time cmplixity 10(N)

#  Inner loop that halves each time 
for i in range(1, n+1):
    j=n
    while j>1:
        j //=2

#  outer = N
# inner = logN
#  time complixity is N * logN

# Progression / Growth pattern 

i =1
while i <=n:
    i *= 2

#  time complixity O(LogN)




#  GP

def geometric_work(N):
    for i in range(1, N + 1):          # Outer loop runs N times
        work_units = 2**i              # 2^1, 2^2, 2^3, ..., 2^N
        
        for j in range(work_units):    # Inner loop scales exponentially
            # O(1) Constant time operation
            print(j)

