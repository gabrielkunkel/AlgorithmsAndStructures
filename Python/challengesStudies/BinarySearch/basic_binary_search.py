from typing import List
import math


class BasicBinarySearch:
    @staticmethod
    def my_attempt(nums: List[int], target: int) -> int:
        if len(nums) == 0:
            return -1

        left, right = 0, len(nums) - 1
        while left <= right:
            midpoint = left + math.floor((right - left) / 2)
            if nums[midpoint] < target:
                left = midpoint + 1
            elif nums[midpoint] > target:
                right = midpoint - 1
            elif nums[midpoint] == target:
                return midpoint

        return -1

    @staticmethod
    def slower_wrong_incrementing(nums: List[int], target: int) -> int:
        """
            This version of binary search is slower and problematic...
            left and right boundaries are adjusted within the loop. In standard binary
            search, you narrow down the search space by half after each comparison,
            which is what gives it O(log n) time complexity.
        :param nums:
        :param target:
        :return:
        """
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (right + left) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = left + 1  # should be midpoint + 1
            else:
                right = right - 1  # should be midpoint - 1

        return -1
