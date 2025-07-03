from typing import List
from collections import deque

class Solution:
    def minFlips(self, mat: List[List[int]]) -> int:
        rows, cols = len(mat), len(mat[0])

        arr = []
        for r in range(rows):
            for c in range(cols):
                arr.append(mat[r][c])
        start = tuple(arr)
        target = tuple([0] * len(arr))

        def get_neighbors(i):
            neighbors = [i]
            r, c = divmod(i, cols)
            if r > 0: neighbors.append((r - 1) * cols + c)     # up
            if r < rows - 1: neighbors.append((r + 1) * cols + c) # down
            if c > 0: neighbors.append(r * cols + (c - 1))     # left
            if c < cols - 1: neighbors.append(r * cols + (c + 1)) # right
            return neighbors

        visited = set()
        queue = deque()
        queue.append((start, 0))
        visited.add(start)

        while queue:
            state, steps = queue.popleft()
            if state == target:
                return steps

            for i in range(len(state)):
                new_state = list(state)
                for j in get_neighbors(i):
                    new_state[j] ^= 1
                t_state = tuple(new_state)
                if t_state not in visited:
                    visited.add(t_state)
                    queue.append((t_state, steps + 1))

        return -1
