"""
Write a function to find the longest common prefix string amongst an array of strings."""
class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        if not strs:
            return ""
        
        prefix = strs[0]  # Start with the first string as the prefix

        for string in strs[1:]:  # Compare with the rest of the strings
            while string[:len(prefix)] != prefix:
                prefix = prefix[:-1]  # Shorten the prefix from the end
                if not prefix:  # If prefix becomes empty, return ""
                    return ""

        return prefix  # Return the longest common prefix
