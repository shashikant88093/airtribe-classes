# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/submissions/2094515181/

class Solution:
    def findMin(self, nums: List[int]) -> int:
        s =0
        e = len(nums) - 1
        while s<e:
            mid = s + (e-s)//2

            if(nums[mid] > nums[e]):
                s = mid + 1
            else:
                e = mid
        return nums[s]
        