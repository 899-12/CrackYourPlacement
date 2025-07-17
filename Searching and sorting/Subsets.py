"""
Given an integer array nums of unique elements, return all possible subsets (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.
"""
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def backtrack(start, path):
            result.append(path[:])  # Add current subset to result
            
            for i in range(start, len(nums)):
                path.append(nums[i])  # Include nums[i] in the subset
                backtrack(i + 1, path)  # Move to the next element
                path.pop()  # Backtrack to explore other subsets
        
        result = []
        backtrack(0, [])
        return result
