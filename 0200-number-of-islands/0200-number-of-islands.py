class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        rows,cols=len(grid),len(grid[0])
        directions=[(-1,0),(0,-1),(1,0),(0,1)]
        islands=0
        def dfs(row,col):
            grid[row][col]='0'
            for dr,dc in directions:
                adjr,adjc=row+dr,col+dc
                if 0<=adjr <rows and 0<=adjc<cols and grid[adjr][adjc]=='1':
                    dfs(adjr,adjc)
        for row in range(rows):
            for col in range(cols):
                if grid[row][col]=='1':
                    islands+=1
                    dfs(row,col)
        return islands