class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        zeros=0
        count=0
        j=0
        for i in range(len(nums)):
            if nums[i]==0:
                zeros+=1
            while zeros>1:
                if nums[j]==0:
                    zeros-=1
                j+=1
            count=max(count,i-j+1-zeros)
        return count-1 if count==len(nums) else count