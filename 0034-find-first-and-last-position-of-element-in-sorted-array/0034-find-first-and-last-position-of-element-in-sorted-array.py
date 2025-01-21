class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        def findPosition(nums, target, findFirst):
            left, right = 0, len(nums) - 1
            pos = -1
            while left <= right:
                mid = left + (right - left) // 2
                if nums[mid] == target:
                    pos = mid
                    if findFirst:
                        right = mid - 1
                    else:
                        left = mid + 1
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return pos

        first = findPosition(nums, target, True)
        last = findPosition(nums, target, False)
        return [first, last]
