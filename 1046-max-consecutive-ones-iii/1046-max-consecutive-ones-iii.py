class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        zeros=0
        count=0
        j=0
        for i in range(len(nums)):
            if nums[i]==0:
                zeros+=1
            while zeros>k:
                if nums[j]==0:
                    zeros-=1
                j+=1
            count=max(count,i-j+1)
        return count