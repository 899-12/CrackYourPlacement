# ARRAYS

## 1. Set Matrix Zeros

### Problem Statement
Given an m x n integer matrix, if an element is 0, set its entire row and column to 0s. The operation must be done in place.

### Constraints
- m == matrix.length
- n == matrix[0].length
- 1 <= m, n <= 200
- -2^31 <= matrix[i][j] <= 2^31 - 1

### Solution

The solution uses the first row and first column of the matrix to mark the rows and columns that need to be zeroed. This approach ensures that the space complexity remains O(1).

### Approach
1. **Initial Check for First Row and First Column**: Determine if the first row and first column contain any zeros.
2. **Mark Zeros Using First Row and First Column**: Use the rest of the matrix to mark rows and columns that need to be zeroed.
3. **Zero Out Cells Based on Markers**: Zero out the necessary cells based on the markers in the first row and column.
4. **Final Zeroing of First Row and First Column**: Zero out the first row and column if they initially contained any zeros.

### Complexity
- **Time Complexity**: \(O(m \times n)\), where \(m\) is the number of rows and \(n\) is the number of columns.
- **Space Complexity**: \(O(1)\) as it uses a constant amount of extra space.

### Code Implementation

```python
from typing import List

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        if not matrix or not matrix[0]:
            return
        
        m, n = len(matrix), len(matrix[0])
        first_row_has_zero = any(matrix[0][j] == 0 for j in range(n))
        first_col_has_zero = any(matrix[i][0] == 0 for i in range(m))
        
        # Use the first row and column to mark zeros
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0
        
        # Zero out cells based on the markers in the first row and column
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
        
        # Zero out the first row if needed
        if first_row_has_zero:
            for j in range(n):
                matrix[0][j] = 0
        
        # Zero out the first column if needed
        if first_col_has_zero:
            for i in range(m):
                matrix[i][0] = 0

# Example usage
solution = Solution()
matrix1 = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
solution.setZeroes(matrix1)
print(matrix1)  # Output: [[1, 0, 1], [0, 0, 0], [1, 0, 1]]
```
## 2.Move Zeroes
### Description
The moveZeroes function is designed to move all zeros in a given integer array nums to the end of the array while maintaining the relative order of the non-zero elements. The function operates in-place, meaning it modifies the input array directly without using extra space for another array.

### Algorithm
The function employs a two-pass approach:

## First Pass:

The function initializes a pointer last_non_zero to track the position where the next non-zero element should be placed.
It iterates through the array and whenever a non-zero element is encountered, it places this element at the position indicated by last_non_zero and increments last_non_zero.
## Second Pass:

After all non-zero elements have been moved to the beginning of the array, the function iterates from the last_non_zero position to the end of the array, filling these positions with zeros.
### Complexity
#### Time Complexity: 
𝑂(𝑛), where 𝑛
n is the number of elements in the array. This is because the function processes each element of the array exactly twice: once to move non-zero elements and once to fill in zeros.
#### Space Complexity: 
𝑂(1), as the function uses a constant amount of extra space regardless of the input size.
