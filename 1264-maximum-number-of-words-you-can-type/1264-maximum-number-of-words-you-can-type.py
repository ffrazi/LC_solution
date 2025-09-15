class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        text=text.split()
        brokenLetters=list(brokenLetters)
        count=len(text)
        for i in range(len(text)):
            curr=text[i]
            for j in range(len(curr)):
                if curr[j] in brokenLetters:
                    count-=1
                    break
        return count