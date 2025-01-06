class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        x=[]
        for i in nums:
            x.append(i*i)
        return sorted(x)