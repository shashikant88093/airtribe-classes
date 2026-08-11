# https://leetcode.com/problems/daily-temperatures/description/


def NGOR(arr):
    stack=[]
    ans = [-1]*len(arr)

    for i in range(len(arr)-1,-1,-1):

        while len(stack) >0 and stack[-1] <=arr[i]:
            stack.pop()
        if len(stack):
            ans[i] =-1
        else:
            ans[i] = stack[-1]
        
        stack.append(arr[i])
    return ans

arr= [2,5,9,3,1,12,6,8,7]

print(arr)

print(NGOR(arr))