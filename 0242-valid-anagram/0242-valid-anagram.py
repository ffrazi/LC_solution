class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        maps={}
        mapt={}
        for char in s:
            maps[char]=maps.get(char,0)+1
        for char in t:
            mapt[char]=mapt.get(char,0)+1
        for key in maps:
            if maps[key]!=mapt.get(key,0):
                return False
        return True

        
        