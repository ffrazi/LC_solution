from collections import deque
from typing import List

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rotten = deque()
        fresh = 0
        rows = len(grid)
        columns = len(grid[0])

        for i in range(rows):
            for j in range(columns):
                if grid[i][j] == 2:
                    rotten.append((i, j, 0))
                elif grid[i][j] == 1:
                    fresh += 1

        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        day = 0

        while rotten:
            r, c, time = rotten.popleft()
            for dr, dc in directions:
                newrow = r + dr
                newcolumn = c + dc
                if 0 <= newrow < rows and 0 <= newcolumn < columns and grid[newrow][newcolumn] == 1:
                    grid[newrow][newcolumn] = 2
                    fresh -= 1
                    rotten.append((newrow, newcolumn, time + 1))
                    day = max(day, time + 1)

        return -1 if fresh > 0 else day
