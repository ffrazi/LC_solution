class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        maxi=0
        sums=0
        mini=0
        for i in range(len(nums)):
            sums+=nums[i]
            maxi=max(sums,maxi)
            mini=min(sums,mini)
        return abs(maxi-mini)