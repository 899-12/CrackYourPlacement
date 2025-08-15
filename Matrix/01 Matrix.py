"""
Given an m x n binary matrix mat, return the distance of the nearest O for
each cell. The distance between two adjacent cells is 1."""
class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        rows, cols = len(mat), len(mat[0])
        dist = [[float('inf')] * cols for _ in range(rows)]
        q = deque()

        # Step 1: Add all 0s to queue
        for r in range(rows):
            for c in range(cols):
                if mat[r][c] == 0:
                    dist[r][c] = 0
                    q.append((r, c))

        # Step 2: BFS from all 0s
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        while q:
            r, c = q.popleft()
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols:
                    if dist[nr][nc] > dist[r][c] + 1:
                        dist[nr][nc] = dist[r][c] + 1
                        q.append((nr, nc))

        return dist
