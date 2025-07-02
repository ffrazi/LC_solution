class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n=len(grid)
        min_heap=[(grid[0][0],0,0)]
        visited=set([(0,0)])
        max_elevation=0
        while True:
            elevation,row,col=heapq.heappop(min_heap)
            max_elevation=max(max_elevation,elevation)
            if row == col == n-1:
                return max_elevation
            for new_row, new_col in[(row+1,col),(row,col+1),(row-1,col),(row,col-1)]:
                if 0<=new_row <n and 0<=new_col <n and (new_row,new_col) not in visited:
                    visited.add((new_row,new_col))
                    heapq.heappush(min_heap,(grid[new_row][new_col],new_row,new_col))