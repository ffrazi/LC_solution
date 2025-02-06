class Solution:
    def countPrimes(self, n: int) -> int:
        if n<2:
            return 0
        arr=[0]*n
        for i in range(2,int(n**0.5)+1):
            if arr[i]==0:
                for j in range(i*i,n,i):
                    arr[j]=1
        return sum(1 for i in range(2,n) if arr[i]==0)