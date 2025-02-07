class Solution:
    def canJump(self, nums: List[int]) -> bool:
        count=0
        for i in nums:
            if count<0:
                return False
            elif i>count:
                count=i
            count-=1
        return True