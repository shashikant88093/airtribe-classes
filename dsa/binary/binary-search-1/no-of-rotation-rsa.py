arr = [4,5,6,7,0,1,2]

def noRSA(arr):
    s =0
    e = len(arr) - 1

    while s<e:
        mid = s + (e - s)//2;
        if(arr[mid] > arr[e]):
            s = mid + 1
        else:  
            e = mid
    return arr[mid]

print(noRSA(arr))


# number is gota