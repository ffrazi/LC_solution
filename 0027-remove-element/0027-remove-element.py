class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        h=[]
        for i in nums:
            if i!=val:
                h.append(i)
        for i in range(len(h)):
            nums[i]=h[i]
        return len(h)