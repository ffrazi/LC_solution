class Solution {
    int diff[][] = new int[][]{{-1,0},{0,-1}};
    public int minPathSum(int[][] grid) {
        int R=grid.length;
        int C=grid[0].length;
        int dp[][]=new int[R][C];
        dp[0][0]=grid[0][0];
        for (int col=1;col<C;col++){
                dp[0][col]=grid[0][col]+dp[0][col-1];
            }
        for (int row=1;row<R;row++){
            dp[row][0] = grid[row][0] + dp[row-1][0];
        }
        for(int row=1;row<R;row++){
            for (int col=1;col<C;col++){
                dp[row][col]=grid[row][col]+Math.min(dp[row-1][col],dp[row][col-1]);
            }
        }
        return dp[R-1][C-1];
    }
}