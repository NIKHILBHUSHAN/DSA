"""
Problem 1: Insertion Sort
LeetCode-style function.

Given a list of integers nums, sort it in ascending order in-place and return it.

Constraints:
- Do not use sorted(), list.sort(), bisect, or any imports.
- Build the sorting logic using comparisons, shifts, and insertion.
"""

class Solution:
    def sortArray(self, nums):
        # Start at index 1: the first element alone is already sorted.
        i = 1

        while i < len(nums):
            key = nums[i]
            j = i - 1

            # Shift every element greater than key one position to the right.
            while j >= 0 and nums[j] > key:
                nums[j + 1] = nums[j]
                j -= 1

            # Insert key into the gap that was created.
            nums[j + 1] = key
            i += 1

        return nums


if __name__ == "__main__":
    solution = Solution()
    nums = [5, 2, 3, 1]
    print(solution.sortArray(nums))  # [1, 2, 3, 5]
