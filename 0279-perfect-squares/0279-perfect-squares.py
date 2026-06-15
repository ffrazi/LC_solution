from collections import deque
import math

class Solution:
    def squares(self,n):
        if n<0:
            return False
        x=int(math.sqrt(n))
        return x*x==n

    def numSquares(self,n:int)->int:
        queue=deque([(n,0)])   # (remaining value, number of squares used)
        vis=set([n])

        while queue:
            rem,cnt=queue.popleft()

            if self.squares(rem):
                return cnt+1

            i=1
            while i*i<=rem:
                nxt=rem-i*i
                if nxt not in vis:
                    vis.add(nxt)
                    queue.append((nxt,cnt+1))
                i+=1