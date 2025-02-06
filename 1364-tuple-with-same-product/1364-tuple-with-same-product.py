class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        count=0
        tracker=collections.Counter()
        for i in range(len(nums)):
            for j in range(i):
                prod=nums[i]*nums[j]
                count+=tracker[prod]*8
                tracker[prod]+=1
        return count