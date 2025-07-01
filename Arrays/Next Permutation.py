class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        
        # Step 1: Find pivot
        pivot = n - 2
        while pivot >= 0 and nums[pivot] >= nums[pivot + 1]:
            pivot -= 1
        
        if pivot >= 0:  # Step 2: Find swap element
            for i in range(n - 1, pivot, -1):
                if nums[i] > nums[pivot]:
                    nums[i], nums[pivot] = nums[pivot], nums[i]
                    break
        
        # Step 3: Reverse suffix
        nums[pivot + 1:] = reversed(nums[pivot + 1:])
