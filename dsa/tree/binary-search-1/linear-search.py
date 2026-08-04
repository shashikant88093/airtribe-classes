

arr = [7,3,1,5,4,2]

def linearSearch(arr,target):
    for num in arr:
        if num == target:
            return True
        
    return False

        
        
print(linearSearch(arr,4))