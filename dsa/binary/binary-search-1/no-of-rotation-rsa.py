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

def binarySearch(arr,k, srange, erange):
        s = srange
        e = erange
        
        while s <= e:
            mid = s + (e - s) // 2
            
            if arr[mid] == k:
                return mid
            elif arr[mid] > k:
                e = mid - 1
            else:
                s = mid + 1
                
        return -1

# Search In RSA

def searchInRSA(arr,key):
    minElementIdx = noRSA(arr)

    bs1 = binarySearch(arr,key,0,minElementIdx-1)
    if bs1 == -1:
        return binarySearch(arr,key,minElementIdx,len(arr)-1)
    return bs1

print(searchInRSA(arr,3))