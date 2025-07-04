class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        i = 0
        patches = 0
        miss = 1  # Smallest number we can't yet form

        while miss <= n:
            if i < len(nums) and nums[i] <= miss:
                # If current number can extend the range
                miss += nums[i]
                i += 1
            else:
                # Patch is needed
                miss += miss
                patches += 1

        return patches
