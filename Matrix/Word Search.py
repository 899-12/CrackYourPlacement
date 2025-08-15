""" 
Given an m xn grid of characters board and a string word, return true if
word exists in the grid.
The word can be constructed from letters of sequentially adjacent cells,
where adjacent cells are horizontally or vertically neighboring. The same
letter cell may not be used more than once.
"""

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
      
        rows, cols = len(board), len(board[0])

        def dfs(r, c, idx):
            if idx == len(word):
                return True
            if (r < 0 or c < 0 or r >= rows or c >= cols or 
                board[r][c] != word[idx]):
                return False

            temp = board[r][c]
            board[r][c] = "#"  # mark as visited

            found = (dfs(r+1, c, idx+1) or
                    dfs(r-1, c, idx+1) or
                    dfs(r, c+1, idx+1) or
                    dfs(r, c-1, idx+1))

            board[r][c] = temp  # restore
            return found

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == word[0] and dfs(r, c, 0):
                    return True
        return False

            
