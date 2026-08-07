

# def binary_Index(arr,key):

#     s =0
#     e =len(arr) -1
#     while(s<=e):

#         mid = s + (e-s)//2

#         if(arr[mid] == key):
#             return mid
#         elif arr[mid] > key:
#             e = mid -1
#         else:
#             s = mid + 1
#     return -1

def first_occurance(arr,key):

    s=0
    e = len(arr) - 1
    ans = -1
    while(s<=e):

        mid = s + (e-s)//2

        if arr[mid]== key:
            ans = mid
            e = mid - 1
        elif arr[mid] < key:
            s = mid + 1
        else:
            e = mid -1
    return ans

def last_occurance(arr,key):
    s=0
    e = len(arr) -1
    ans = -1
    while(s<=e):

        mid = s + (e-s)//2

        if arr[mid] == key:
            ans = mid
            s = mid + 1
        elif arr[mid] < key:
            s = mid + 1
        else:
            e = mid -1
    return ans

def count_occurance(arr,key):
    fo = first_occurance(arr,key)
    lo = last_occurance(arr,key)
    if fo == -1:
        return -1
        
    return lo - fo + 1 


arr = [2,2,3,3,3,3,4,4,4,4,7]

print(count_occurance(arr,3))