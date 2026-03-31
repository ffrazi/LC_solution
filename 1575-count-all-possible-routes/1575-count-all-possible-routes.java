class Solution{
    static int MOD=1000000007;

    public int countRoutes(int[] l,int s,int e,int fuel){
        int n=l.length;
        Integer[][] dp=new Integer[n][fuel+1];
        return f(l,s,e,fuel,dp);
    }

    int f(int[] l,int c,int e,int fuel,Integer[][] dp){
        if(fuel<0)return 0;
        if(dp[c][fuel]!=null)return dp[c][fuel];

        int ans=c==e?1:0;

        for(int i=0;i<l.length;i++){
            if(i!=c){
                int d=Math.abs(l[i]-l[c]);
                if(fuel>=d)ans=(ans+f(l,i,e,fuel-d,dp))%1000000007;
            }
        }

        return dp[c][fuel]=ans;
    }
}