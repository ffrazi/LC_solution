class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        h=[]
        for i in nums:
            if i not in h:
                h.append(i)
        for i in range(len(h)):
            nums[i]=h[i]
        return len(h)