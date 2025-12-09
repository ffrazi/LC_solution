class Solution {
    long[] dp;

    public int climbStairs(int n) {
        dp = new long[n + 1];
        Arrays.fill(dp, -1);
        return (int) climb(n);
    }

    private long climb(int n) {
        if (n <= 2) return n;
        if (dp[n] != -1) return dp[n];
        dp[n] = climb(n - 1) + climb(n - 2);
        return dp[n];
    }
}
