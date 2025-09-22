class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        count=Counter(nums)
        maxfeq=max(count.values())
        return sum(i for i in count.values() if i==maxfeq)