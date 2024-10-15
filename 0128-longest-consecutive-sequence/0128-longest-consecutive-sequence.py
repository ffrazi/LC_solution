class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset=set(nums)
        max_len=0
        for i in numset:
            if (i-1) not in numset:
                length=1
                while(i+length) in numset:
                    length+=1
                max_len=max(length,max_len)
        return max_len        