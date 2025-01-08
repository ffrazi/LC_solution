class Solution:
    def removeDuplicates(self, s: str) -> str:
        s=list(s)
        i=0
        while i<len(s)-1:
            if s[i]==s[i+1]:
                del s[i:i+2]
                i=max(i-1,0)
            else:
                i+=1
        return "".join(s)        