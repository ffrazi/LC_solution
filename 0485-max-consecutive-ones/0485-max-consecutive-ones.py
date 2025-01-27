class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count=0
        j=0
        for i in range(len(nums)):
            if nums[i]==0:
                j=i+1
            else:
                count=max(count,i-j+1)
        return count