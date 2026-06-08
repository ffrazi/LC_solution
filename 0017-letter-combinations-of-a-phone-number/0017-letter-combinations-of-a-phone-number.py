class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        combos={"2":"abc","3":"def","4":"ghi","5":"jkl","6":"mno","7":"pqrs","8":"tuv","9":"wxyz"}
        ans=[]
        def backtrack(i,curr):
            if i==len(digits):
                ans.append(curr)
                return
            for j in combos[digits[i]]:
                backtrack(i+1,curr+j)
        backtrack(0,"")
        return ans 