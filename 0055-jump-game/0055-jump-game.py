class Solution:
    def canJump(self, nums: List[int]) -> bool:
        maxreach=0
        reach=0
        for re in range(0,len(nums)-1):
            if re>maxreach:
                return False
            reach=re+nums[re]
            maxreach=max(reach,maxreach)
        if maxreach>=len(nums)-1:
            return True
        else:
            return False