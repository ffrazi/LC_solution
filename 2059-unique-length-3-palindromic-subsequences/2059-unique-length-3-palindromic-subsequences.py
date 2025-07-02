class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        first = [float('inf')] * 26
        last = [-1] * 26
        result = 0

        for i, ch in enumerate(s):
            idx = ord(ch) - ord('a')
            first[idx] = min(first[idx], i)
            last[idx] = max(last[idx], i)

        for i in range(26):
            if first[i] < last[i]:
                middle_chars = set(s[first[i] + 1:last[i]])
                result += len(middle_chars)

        return result
