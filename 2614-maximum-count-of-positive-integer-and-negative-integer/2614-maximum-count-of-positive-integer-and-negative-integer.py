class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        countpos=0
        countneg=0
        for i in range(len(nums)):
            if nums[i]==0:
                pass
            elif nums[i]<0:
                countneg+=1
            else:
                countpos+=1
        return (max(countneg,countpos))