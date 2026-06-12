class Solution:
    def lcs(self,t1,t2,i,j,dp):
        if i==-1 or j==-1:
            return 0

        if dp[i][j]!=-1:
            return dp[i][j]

        if t1[i]==t2[j]:
            dp[i][j]=1+self.lcs(t1,t2,i-1,j-1,dp)

        else:
            dp[i][j]=max(
                self.lcs(t1,t2,i,j-1,dp),
                self.lcs(t1,t2,i-1,j,dp)
            )

        return dp[i][j]

    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m=len(text1)
        n=len(text2)
        dp=[[-1]*n for _ in range(m)]
        return self.lcs(text1,text2,m-1,n-1,dp)