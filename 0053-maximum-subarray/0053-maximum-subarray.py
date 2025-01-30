class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        sums=0
        maxi=-inf
        for i in nums:
            sums=max(i,sums+i)
            maxi=max(sums,maxi)
        return maxi