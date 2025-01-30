class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        freq = [0] * 26 
        for c in s1:
            freq[ord(c) - ord('a')] -= 1
        for i in range(len(s1)):
            freq[ord(s2[i]) - ord('a')] += 1
        diff = sum(1 for x in freq if x != 0)

        for i in range(len(s1), len(s2)):
            if diff == 0:
                return True
            add_idx = ord(s2[i]) - ord('a')
            if freq[add_idx] == 0:
                diff += 1
            freq[add_idx] += 1
            if freq[add_idx] == 0:
                diff-=1
            remove_idx = ord(s2[i - len(s1)]) - ord('a')
            if freq[remove_idx] == 0:
                diff += 1
            freq[remove_idx] -= 1
            if freq[remove_idx] == 0:
                diff -= 1

        return diff == 0