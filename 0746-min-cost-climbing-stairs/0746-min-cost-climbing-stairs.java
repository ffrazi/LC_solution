class Solution {
    //memonization
    int[] dp;
    public int minCostClimbingStairs(int[] cost) {
        int n = cost.length;
        dp = new int[n];
        Arrays.fill(dp,-1);
        return Math.min(solve(n-1,cost),solve(n-2,cost));
    }
    private int solve(int i ,int[] cost){
        if (i<=1) return cost[i];
        if(dp[i]!=-1) return dp[i];
        dp[i]=cost[i]+Math.min(solve(i-1,cost),solve(i-2,cost));
        return dp[i];
    }
}