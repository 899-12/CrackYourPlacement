"""
Valid Sudoku"""
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]  # 3×3 sub-boxes

        for r in range(9):
            for c in range(9):
                val = board[r][c]
                if val == '.':
                    continue
                
                # Box index: 0 to 8
                box_index = (r // 3) * 3 + (c // 3)
                
                # Check duplicates
                if (val in rows[r]) or (val in cols[c]) or (val in boxes[box_index]):
                    return False
                
                # Record the value
                rows[r].add(val)
                cols[c].add(val)
                boxes[box_index].add(val)
        
        return True
