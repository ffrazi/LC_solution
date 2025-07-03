from collections import deque
from typing import List

class Solution:
    def shortestPathAllKeys(self, grid: List[str]) -> int:
        R, C = len(grid), len(grid[0])
        total_keys = 0
        queue = deque()
        visited = [[[False] * (1 << 6) for _ in range(C)] for _ in range(R)]

        # Find starting point and count keys
        for row in range(R):
            for col in range(C):
                ch = grid[row][col]
                if ch == '@':
                    queue.append((row, col, 0, 0))  # row, col, steps, keys bitmask
                    visited[row][col][0] = True
                elif 'a' <= ch <= 'f':
                    total_keys += 1

        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        final_key_mask = (1 << total_keys) - 1

        while queue:
            r, c, steps, keys = queue.popleft()

            if keys == final_key_mask:
                return steps

            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                if 0 <= nr < R and 0 <= nc < C:
                    ch = grid[nr][nc]
                    if ch == '#':
                        continue

                    new_keys = keys
                    if 'a' <= ch <= 'f':
                        new_keys |= 1 << (ord(ch) - ord('a'))

                    if 'A' <= ch <= 'F' and not (keys & (1 << (ord(ch) - ord('A')))):
                        continue  # locked door without key

                    if not visited[nr][nc][new_keys]:
                        visited[nr][nc][new_keys] = True
                        queue.append((nr, nc, steps + 1, new_keys))

        return -1
