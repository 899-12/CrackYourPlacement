class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        def countLessEqual(mid):
            count, n = 0, len(matrix)
            row, col = n - 1, 0

            while row >= 0 and col < n:
                if matrix[row][col] <= mid:
                    count += row + 1
                    col += 1
                else:
                    row -= 1
            return count

        start, end = matrix[0][0], matrix[-1][-1]
        while start < end:
            mid = (start + end) // 2
            if countLessEqual(mid) < k:
                start = mid + 1
            else:
                end = mid

        return start
