class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        ans=[]
        for i in candies:
            res=True
            for j in candies:
                if i+extraCandies<j:
                    res=False
            ans.append(res)
        return ans