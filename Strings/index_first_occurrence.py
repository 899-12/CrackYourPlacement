""" Given two strings needle and haystack, return the
   index of the first occurrence of needle in haystack, or
  -1 if needle is not part of haystack.
"""

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        len_h, len_n = len(haystack), len(needle)
        
        for i in range(len_h - len_n + 1):  
            if haystack[i:i+len_n] == needle:  
                return i  
        
        return -1 


"""Using find
Time Complexity:
✅ O(N) in the worst case (where N is the length of haystack).

Space Complexity:
✅ O(1) (no extra space is used).
"""

def strStr(haystack: str, needle: str) -> int:
    return haystack.find(needle)  # Returns the index of the first occurrence, or -1 if not found

# Example Usage
print(strStr("sadbutsad", "sad"))  # Output: 0
print(strStr("leetcode", "leeto")) # Output: -1
