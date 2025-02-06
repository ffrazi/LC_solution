class Solution {
    public int countPrimes(int n) {
        if(n==0 || n==1)
        {
            return 0;
        }
        boolean prime[] = new boolean[n+1];
        for(int ctr=2;ctr<=n;ctr++)
        {
            prime[ctr]=true;
        }
        for(int ctr=4;ctr<=n;ctr+=2)
        {
            prime[ctr]=false;
        }
        for(int ctr=3;ctr*ctr<=n;ctr++)
        {
            if(!prime[ctr])
            {
                continue;
            }
            for(int val=2*ctr;val<=n;val+=ctr)
            {
                prime[val]=false;
            }
        }
        int primes=0;
        for(int num=2;num<n;num++)
        {
            if(prime[num])
            {
                primes++;
            }
        }
        return primes;
    }
}