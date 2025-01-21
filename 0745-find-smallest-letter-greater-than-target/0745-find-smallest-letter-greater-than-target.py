class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        targetord=ord(target)-ord('a')
        for i in letters:
            letterord =ord(i)-ord('a')
            if letterord>targetord:
                return i
        return letters[0]
