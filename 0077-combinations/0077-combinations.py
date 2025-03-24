class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res=[]
        combo=[]
        def backtracking(start):
            if len(combo)==k:
                res.append(combo[:])
                return
            for num in range(start,n+1):
                combo.append(num)
                backtracking(num+1)
                combo.pop()
        backtracking(1)
        return res
