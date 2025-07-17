"""
Given n pairs of parentheses, 
write a function to generate all combinations of well-formed parentheses."""
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result=[]

        def backtrack(curr,open,close_count):
            if len(curr)==2*n:
                result.append(curr)
                return
            
            if open<n:
                backtrack(curr+"(",open+1,close_count)
            if close_count<open:
                backtrack(curr+")",open,close_count+1)
        

        backtrack("",0,0)
        return result

        
