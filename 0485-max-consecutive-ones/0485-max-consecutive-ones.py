class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count=window=0
        for i in nums:
            if i==1:
                window+=1
            else:
                count=max(count,window)
                window=0
        count=max(count,window)
        return count