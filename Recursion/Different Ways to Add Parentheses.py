"""
Given a string expression of numbers and operators, return all possible results from computing all the different possible ways to group numbers and operators. You may return the answer in any order.

The test cases are generated such that the output values fit in a 32-bit integer and the number of different results does not exceed 104"""
class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
            memo = {}

            def ways(expr):
                if expr in memo:
                    return memo[expr]
                
                res = []
                for i, char in enumerate(expr):
                    if char in "+-*":
                        left = ways(expr[:i])
                        right = ways(expr[i+1:])
                        
                        for l in left:
                            for r in right:
                                if char == '+':
                                    res.append(l + r)
                                elif char == '-':
                                    res.append(l - r)
                                elif char == '*':
                                    res.append(l * r)
                
                # If no operator found, it’s a number
                if not res:
                    res.append(int(expr))

                memo[expr] = res
                return res

            return ways(expression)

        
