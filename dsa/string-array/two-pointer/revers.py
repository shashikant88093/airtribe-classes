
arr = [1,4,6,7,8,9,6,2]

class Reverse:

    def reverseArray(self,arr):
        i =0
        j =len(arr) - 1



    def swap(self,arr,i,j):
        temp = arr[i]
        arr[i] = arr[j]
        arr[j] = temp




# reverse string

obj = Reverse(arr)

print(obj)