class Solution:
    def isValid(self, s: str) -> bool:  # Added 'self' parameter
        stack = []
        bracket_map = {')': '(', '}': '{', ']': '['}  

        for char in s:
            if char in bracket_map:  
                top_element = stack.pop() if stack else '#'  
                if top_element != bracket_map[char]:  
                    return False
            else:
                stack.append(char)  

        return not stack  # Return True if stack is empty (valid), else False


solution = Solution()
