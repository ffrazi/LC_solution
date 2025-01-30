class Solution:
    def arraySign(self, nums: List[int]) -> int:
        x=1
        for i in range(len(nums)):
            x*=nums[i]
        if x<0:
            return -1
        elif x==0:
            return 0
        return 1