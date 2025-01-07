class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        r=[]
        for i in range(len(words)):
            for j in range(len(words)):
                if i==j:
                    continue
                if words[i] in words[j]:
                    r.append(words[i])
                    break                  
        return r