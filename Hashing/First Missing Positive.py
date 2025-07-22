"""
Given an unsorted integer array nums. Return the smallest positive integer that is not present in nums.

You must implement an algorithm that runs in O(n) time and uses O(1) auxiliary space."""
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
      
        n = len(nums)

        # Step 1: Place nums[i] in its correct index if possible
        for i in range(n):
            while 1 <= nums[i] <= n and nums[nums[i]-1] != nums[i]:
                correct_idx = nums[i] - 1
                nums[i], nums[correct_idx] = nums[correct_idx], nums[i]

        # Step 2: Find the first location where nums[i] != i + 1
        for i in range(n):
            if nums[i] != i + 1:
                return i + 1

        # Step 3: All numbers from 1 to n are present
        return n + 1
