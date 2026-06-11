class Solution {
    int[][] dp;
    int fun(int i,int j,int[][] obstacleGrid){
        if (i<0 || j<0)
            return 0;
        if(obstacleGrid[i][j]==1)
            return 0;
        if(i==0 && j==0)
            return 1;
        if (dp[i][j]!=-1)
            return dp[i][j];
        return dp[i][j]=fun(i-1,j,obstacleGrid)+fun(i,j-1,obstacleGrid);
    }
    public int uniquePathsWithObstacles(int[][] obstacleGrid) {
        int m=obstacleGrid.length;
        int n=obstacleGrid[0].length;
        dp = new int[m][n];
        for(int i=0;i<m;i++){
            Arrays.fill(dp[i],-1);
        }
        return fun(m-1,n-1,obstacleGrid);
    }
}