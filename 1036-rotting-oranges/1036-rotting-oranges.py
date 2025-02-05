from collections import deque

class Orange:
    def __init__(self, row, col, days):
        self.row = row
        self.col = col
        self.days = days

class Solution:
    def orangesRotting(self, grid):
        R, C = len(grid), len(grid[0])
        visited = [[False] * C for _ in range(R)]
        queue = deque()
        days, oranges = 0, 0

        for row in range(R):
            for col in range(C):
                if grid[row][col] != 0:
                    if grid[row][col] == 2:
                        queue.append(Orange(row, col, 0))
                        visited[row][col] = True
                    oranges += 1

        if oranges == 0:
            return 0  

        directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]

        while queue:
            rotten = queue.popleft()
            oranges -= 1
            days = max(days, rotten.days)

            for dr, dc in directions:
                adjR, adjC = rotten.row + dr, rotten.col + dc

                if 0 <= adjR < R and 0 <= adjC < C:
                    if grid[adjR][adjC] == 1 and not visited[adjR][adjC]:
                        queue.append(Orange(adjR, adjC, rotten.days + 1))
                        visited[adjR][adjC] = True
                        grid[adjR][adjC] = 2  

        return -1 if oranges > 0 else days
