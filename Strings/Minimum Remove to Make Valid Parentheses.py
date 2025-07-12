"""Given a string s of '(' , ')' and lowercase English characters.

Your task is to remove the minimum number of parentheses ( '(' or ')', in any positions ) so that the resulting parentheses string is valid and return any valid string.

"""
class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack=[]
        to_remove=set()

        for i,char in enumerate(s):
            if char=='(':
                stack.append(i)
            elif char==')':
                if stack:
                    stack.pop()
                else:
                    to_remove.add(i)
            
        to_remove=to_remove.union(set(stack))
            # Build the result string
        result = []
        for i, char in enumerate(s):
            if i not in to_remove:
                result.append(char)

        return ''.join(result)
