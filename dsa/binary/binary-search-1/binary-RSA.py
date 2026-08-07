
# arr= [8,12,20,25,3,5,7]

# min = arr[0]

# for i in range(len(arr)):
#     # print(arr[i])
#     if(arr[i] <min):
#         min = arr[i]
    

# print(min)


def rsa_binary(arr):

    s=0
    e = len(arr) - 1

    while(s<e):
        
        mid = s + (e-s)//2

        if arr[mid] > arr[e]:
            s = mid +1
        else:
            e = mid
    return arr[s]
arr = [7,12,20,30,32]

print(rsa_binary(arr))