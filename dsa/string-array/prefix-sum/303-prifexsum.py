#  ================================= brut force ====================================

# Input
# ["NumArray", "sumRange", "sumRange", "sumRange"]
# [[[-2, 0, 3, -5, 2, -1]], [0, 2], [2, 5], [0, 5]]
# Output
# [null, 1, -1, -3]


queries = [
    [0,2],
    [2,5],
    [0,5]
]

arr = [-2,0,3,-5,2,-1]

# # sum = 0

# result =[None]
# for j in range(len(queries)):
#     # print(queries[j],"arr[j]")
#     L = queries[j][0]
#     R = queries[j][1]
#     sum=0
#     print(sum,"one loop")
#     for i in range(L,R + 1):
#         sum += arr[i]
#     result.append(sum)

# print(result)

#  =========================== optimize version ======================================

# class prefixSum:
#     def __init__(self,sums,queries):
#         self.sums = sums
#         self.prefix_sum = [0] * len(sums)
#         self.queries = queries
#         # print(self.prefix_sum)
#         for i in range(len(queries)):
#             # print(queries[i])
#             self.sumRange(queries[i][0],queries[i][1])


#     def sumRange(self,left,right):
#         print(left,right)
#         result = [None]
#         sum =0

#         for j in range(right,left -1 ):

#             # print(self.sums[j])
#             if(left==0):
#                 sum += self.sums[j]
#             else:
#                 pass
#                 # sum += (self.sums[right] + self.sums[left - 1])
#         print(sum)
                
#         result.append(sum)
#         # print(result)
#         return result

# obj = prefixSum(arr,queries)

# print(obj)


class NumArray:
    def __init__(self, nums: list[int]):
        self.arr = nums  # This step outputs: null

    def sumRange(self, left: int, right: int) -> int:
        query_sum = 0
        
        # Loop strictly from left to right
        for i in range(left, right + 1):
            query_sum += self.arr[i]
            
        return query_sum  # This step outputs your numbers: 1, -1, -3


# 1. अपना असली Array देकर Object बनाइए
arr = [-2, 0, 3, -5, 2, -1]

obj = NumArray(arr)

# 2. अब obj के अंदर से sumRange फंक्शन को बुलाइए और Print करिए
print(obj.sumRange(0, 2))  # आउटपुट आएगा: 1
print(obj.sumRange(2, 5))  # आउटपुट आएगा: -1
print(obj.sumRange(0, 5))  # आउटपुट आएगा: -3
        
