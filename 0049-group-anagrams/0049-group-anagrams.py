class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap=defaultdict(list)
        for words in strs:
            count=[0]*26
            for char in words:
                count[ord(char)-ord('a')]+=1
            hashmap[tuple(count)].append(words)
        return hashmap.values()