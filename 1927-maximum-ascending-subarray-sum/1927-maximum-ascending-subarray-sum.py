from typing import List

class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        maxsum = nums[0]
        count = nums[0]
        
        for i in range(1, len(nums)):
            if nums[i-1] < nums[i]:  
                count += nums[i]
            else:
                maxsum = max(maxsum, count)  
                count = nums[i]
        return max(maxsum, count)