class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        count=0
        x=[]
        for i in range(len(nums)):
            count+=nums[i]
            x.append(count)
        return x