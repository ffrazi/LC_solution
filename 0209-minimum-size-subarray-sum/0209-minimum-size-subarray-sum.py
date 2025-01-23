class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        min_len = float('inf')
        i=0
        min_sum=0
        for j in range(len(nums)):
            min_sum+=nums[j]
            while min_sum>=target:
                if j-i+1<min_len:
                    min_len=j-i+1
                min_sum -=nums[i]
                i+=1
        return min_len if min_len != float('inf') else 0