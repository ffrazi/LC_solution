class Solution(object):
    def findGCD(self, nums):
        a,b=min(nums),max(nums)
        while a!=b:
            b=b-a
            a,b=min(a,b),max(a,b)
        return a     