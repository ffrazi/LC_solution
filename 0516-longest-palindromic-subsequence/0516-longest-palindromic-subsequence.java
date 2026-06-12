class Solution {
    int[][] dp;

    public int LPS(String s,int start,int end){
        if(start>end)
            return 0;

        if(start==end)
            return 1;

        if(dp[start][end]!=-1)
            return dp[start][end];

        if(s.charAt(start)==s.charAt(end))
            return dp[start][end]=2+LPS(s,start+1,end-1);

        return dp[start][end]=Math.max(LPS(s,start,end-1),LPS(s,start+1,end));
    }

    public int longestPalindromeSubseq(String s) {
        int n=s.length();
        dp=new int[n][n];

        for(int i=0;i<n;i++){
            Arrays.fill(dp[i],-1);
        }

        return LPS(s,0,n-1);
    }
}