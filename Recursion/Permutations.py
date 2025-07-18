"""
Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order."""
from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []

        def backtrack(path, used):
            if len(path) == len(nums):
                result.append(path[:])
                return
            
            for i in range(len(nums)):
                if used[i]:
                    continue
                # Choose
                path.append(nums[i])
                used[i] = True
                # Explore
                backtrack(path, used)
                # Un-choose (backtrack)
                path.pop()
                used[i] = False

        backtrack([], [False] * len(nums))
        return result
