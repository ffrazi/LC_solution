from collections import Counter
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransom=Counter(ransomNote)
        magazines =Counter(magazine)
        for i,j in ransom.items():
            if magazines[i] < j:
                return False
        return True