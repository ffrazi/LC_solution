class Solution:
    def firstMissingPositive(self, nums):
        num = sorted(set([x for x in nums if x > 0]))  # Remove duplicates and sort
        if not num or num[0] != 1:
            return 1
        for i in range(len(num) - 1):
            if num[i + 1] != num[i] + 1:
                return num[i] + 1
        return num[-1] + 1
