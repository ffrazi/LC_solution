class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        if k==0:
            return nums
        nums[::]=[nums[i-k] for i in range(len(nums))]