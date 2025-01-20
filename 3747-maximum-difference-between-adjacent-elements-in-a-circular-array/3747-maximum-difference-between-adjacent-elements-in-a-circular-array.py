class Solution:
    def maxAdjacentDistance(self, nums: List[int]) -> int:
        n = len(nums)
        maxdiff = 0
        for i in range(n):
            diff = abs(nums[i] - nums[(i + 1) % n])
            maxdiff = max(maxdiff, diff)
        return maxdiff
