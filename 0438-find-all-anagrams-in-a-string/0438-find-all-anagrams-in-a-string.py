class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        p=''.join(sorted(p))
        window=''
        start_indices=[]
        start=0
        for i in s:
            window+=i
            if len(window)==len(p):
                if ''.join(sorted(window))==p:
                    start_indices.append(start)
                window=window[1:]
                start+=1
        return start_indices