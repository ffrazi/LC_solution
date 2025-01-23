class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        count=0
        m=len(grid)
        n=len(grid[0])
        row=[0]*m
        column=[0]*n
        for i in range(m):
            for j in range(n):
                if grid[i][j]==1:
                    row[i]+=1
                    column[j]+=1
        for i in range(m):
            for j in range(n):
                if grid[i][j]==1:
                    if row[i]>1 or column[j]>1:
                        count+=1
        return count