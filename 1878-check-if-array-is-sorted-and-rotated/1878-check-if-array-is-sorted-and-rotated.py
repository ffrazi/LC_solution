class Solution:
    def check(self, nums: List[int]) -> bool:
        count=0
        for i,v in enumerate(nums):
            if nums[i-1]>v:
                count+=1
        return count<=1