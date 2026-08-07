
def first(arr,key):

    s = 0
    e = len(arr) - 1
    ans = -1
    while(s<=e):

        mid = s + (e-s)//2

        if arr[mid] == key:
            ans = mid
            e = mid -1
        elif arr[mid] < key:
            s = mid + 1
        else:
            e = mid - 1
    return ans

def last(arr,key):

    s = 0
    e = len(arr) - 1
    ans = -1
    while(s<=e):

        mid = s + (e-s)//2

        if arr[mid] == key:
            ans = mid
            s = mid + 1
        elif arr[mid] < key:
            s = mid + 1
        else:
            e = mid - 1
    return ans

def position_index(arr,key):
    fo = first(arr,key)
    lo = last(arr,key)
    print(fo ,lo)
    if fo == -1:
        return [-1,-1]
    return [fo,lo]

arr = [5,7,7,8,8,10]

print(position_index(arr,8))

