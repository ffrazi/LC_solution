class Solution:
    def sortVowels(self, s: str) -> str:
        vowels=['a','e','i','o','u','A','E','I','O','U']
        t=""
        v=[]
        for i in range(len(s)):
            if s[i] in vowels:
                v.append(s[i])
        v.sort(reverse=True)
        #return v
        for i in range(len(s)):
            if s[i] not in vowels:
                t+=s[i]
            else:
                t+=v[-1]
                v.pop()
        return t
