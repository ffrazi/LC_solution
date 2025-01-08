class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        count=0
        for i in range(len(words)):
            s1=words[i]
            for j in range(i+1,len(words)):
                s2=words[j]
                if len(s2)<len(s1):
                    continue
                pre=s2[:len(s1)]
                suf=s2[-len(s1):]
                if pre==s1 and suf==s1:
                    count+=1
        return count