## Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

##The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

## You must write an algorithm that runs in O(n) time and without using the division operation.##


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n=len(nums)
        left=[1]*n
        right=[1]*n
        output=[0]*n
        for i in range(1,n):
            left[i]=left[i-1]*nums[i-1]
        for j in range(n-2,-1,-1):
            right[j]=right[j+1]*nums[j+1]

        for i in range(n):
            output[i]=left[i]*right[i]
        return output
        
