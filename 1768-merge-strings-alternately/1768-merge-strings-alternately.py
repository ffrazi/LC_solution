class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        new=""
        l=min(len(word1),len(word2))
        for i in range(l):
            new+=word1[i]
            new+=word2[i]
        if len(word1)>len(word2):
            new+=word1[l:]
        else:
            new+=word2[l:]
        return new