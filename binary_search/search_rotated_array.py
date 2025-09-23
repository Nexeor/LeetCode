from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            m = (l + r) // 2
            if nums[m] == target:
                return m
            # Mid in left portion
            elif nums[l] <= nums[m]:
                # Target greater than mid or in right portion -> move right
                if target > nums[m] or target < nums[l]:
                    l = m + 1
                # Target within [L, M] -> move left
                else:
                    r = m - 1
            # Mid in right portion
            else:
                # Target less than mid or in left portion -> move left
                if target < nums[m] or target > nums[r]:
                    r = m - 1
                # Target within [M, R] -> move right
                else:
                    l = m + 1

        return -1
