class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def backtracking(sol):
            if len(sol)==len(nums):
                res.append(sol[:])
                return
            for num in nums:
                if num not in sol:
                    sol.append(num)
                    backtracking(sol)
                    sol.pop()
        res=[]
        backtracking([])
        return res