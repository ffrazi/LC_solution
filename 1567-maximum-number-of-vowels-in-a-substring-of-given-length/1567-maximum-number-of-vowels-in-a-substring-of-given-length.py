class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels={'a', 'e', 'i', 'o','u'}
        total=0
        for ch in s[0:k]:
            if ch in vowels:
                total+=1
        maxcnt=total
        i=0
        for j in range(k,len(s)):
            if s[j] in vowels:
                total+=1
            if s[i] in vowels:
                total-=1
            i+=1
            maxcnt=max(maxcnt,total)
        return maxcnt