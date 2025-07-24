"""
You are given a 0-indexed, strictly increasing integer array nums and a positive integer diff.
A triplet (i, j, k) is an arithmetic triplet if the following conditions are met"""

class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        num_set = set(nums)
        count = 0
        for num in nums:
            if (num - diff in num_set) and (num - 2 * diff in num_set):
                count += 1
        return count

        
