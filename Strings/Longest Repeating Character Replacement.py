"""
You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most k times.

Return the length of the longest substring containing the same letter you can get after performing the above operations."""



class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        from collections import defaultdict
        count = defaultdict(int)
        max_freq = 0
        left = 0
        res = 0

        for right in range(len(s)):
            count[s[right]] += 1
            max_freq = max(max_freq, count[s[right]])

            while (right - left + 1) - max_freq > k:
                count[s[left]] -= 1
                left += 1

            res = max(res, right - left + 1)

        return res
