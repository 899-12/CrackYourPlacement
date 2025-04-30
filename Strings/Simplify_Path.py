"""
LeetCode Problem 71: Simplify Path
Link: https://leetcode.com/problems/simplify-path/

🧩 Description:
Given an absolute path for a Unix-style file system, simplify it to its canonical path.

Rules:
- '.' : current directory
- '..' : parent directory
- Multiple slashes '//' are treated as a single '/'
- Canonical path:
    - Starts with '/'
    - No trailing slash (unless it's root)
    - No '.' or '..' in path

🧪 Examples:
Input: "/home/"
Output: "/home"

Input: "/../"
Output: "/"

Input: "/home//foo/"
Output: "/home/foo"

Input: "/a/./b/../../c/"
Output: "/c"
"""
class Solution:
    def simplifyPath(self, path: str) -> str:
        stack=[]
        parts=path.split("/")

        for part in parts:
            if part=="" or part ==".":
                continue
            elif part=="..":
                if stack:
                    stack.pop()
            else:
                stack.append(part)
        return "/" + "/".join(stack)
