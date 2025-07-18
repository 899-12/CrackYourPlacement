"""
Given a string s, partition s such that every substring of the partition is a palindrome. Return all possible palindrome partitioning of s.

 
"""
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def is_palindrome(sub):
            return sub == sub[::-1]  # Check if substring is a palindrome
        
        def backtrack(start, path):
            if start == len(s):  # If we've partitioned the entire string
                result.append(path[:])
                return
            
            for end in range(start + 1, len(s) + 1):
                substring = s[start:end]
                if is_palindrome(substring):  # Only proceed if it's a palindrome
                    path.append(substring)
                    backtrack(end, path)  # Explore further partitions
                    path.pop()  # Undo the choice
        
        result = []
        backtrack(0, [])
        return result
