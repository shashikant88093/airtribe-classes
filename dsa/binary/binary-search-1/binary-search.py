# arr = [5,10,15,20,25,30]



# def binarySearch(arr,key):
#     s=0;
#     e= len(arr) - 1

#     while s<=e:
#         mid = (s+e)//2

#         if arr[mid] ==key:
#             return True
#         if arr[mid]>key:
#             e = mid -1
#         else:
#             s = mid+1
#     return False

# print(binarySearch(arr,20))


#  question 
#  https://www.geeksforgeeks.org/problems/who-will-win-1587115621/1


class Solution:
    def binarySearch(self, arr: list[int], k: int) -> bool:
        s = 0
        e = len(arr) - 1
        
        while s <= e:
            mid = s + (e - s) // 2
            
            if arr[mid] == k:
                return mid
            elif arr[mid] > k:
                e = mid - 1
            else:
                s = mid + 1
                
        return -1

# --- Driver Code Example ---
# arr = [2, 5, 8, 12, 16, 23, 38, 56, 72]
arr = [1,2,4,5,6]
# k = 23
k=3

obj = Solution()
result = obj.binarySearch(arr, k)

print(result)  # Output: True