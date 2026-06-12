class Solution {
    int[][] dp;

    public int LCS(String s1,String s2,int i,int j){
        if(i<0 || j<0)
            return 0;

        if(dp[i][j]!=-1)
            return dp[i][j];

        if(s1.charAt(i)==s2.charAt(j))
            return dp[i][j]=1+LCS(s1,s2,i-1,j-1);

        return dp[i][j]=Math.max(LCS(s1,s2,i-1,j),LCS(s1,s2,i,j-1));
    }

    public int minDistance(String word1, String word2) {
        int m=word1.length();
        int n=word2.length();

        dp=new int[m][n];

        for(int i=0;i<m;i++)
            Arrays.fill(dp[i],-1);

        int lcs=LCS(word1,word2,m-1,n-1);

        return m+n-2*lcs;
    }
}