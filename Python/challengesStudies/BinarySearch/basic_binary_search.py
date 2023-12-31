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
