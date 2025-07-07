"""
Given an array of positive integers nums and a positive integer target,
return the minimal length of a subarray whose sum is greater than or equal to target.

If there is no such subarray, return 0 instead.

Example:
Input: target = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: The subarray [4,3] has the minimal length under the problem constraint.
"""
def minSubArrayLen(target, nums):
    n = len(nums)
    left = 0
    total = 0
    min_len = float('inf')

    for right in range(n):
        total += nums[right]

        # Shrink the window from the left while total >= target
        while total >= target:
            min_len = min(min_len, right - left + 1)
            total -= nums[left]
            left += 1

    return 0 if min_len == float('inf') else min_len
