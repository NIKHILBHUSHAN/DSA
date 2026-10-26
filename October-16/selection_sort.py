"""
LeetCode-style Problem: Selection Sort

Implement selection sort from scratch.
Forbidden: sort(), sorted(), min(), and imports.
"""


class Solution:
    def selectionSort(self, nums: list) -> list:
        n = len(nums)

        for i in range(n):
            smallest_index = i

            # Scan the unsorted portion to find the smallest value.
            for j in range(i + 1, n):
                if nums[j] < nums[smallest_index]:
                    smallest_index = j

            # Swap the smallest value into its correct position.
            if smallest_index != i:
                temp = nums[i]
                nums[i] = nums[smallest_index]
                nums[smallest_index] = temp

        return nums


if __name__ == "__main__":
    solution = Solution()
    print(solution.selectionSort([64, 25, 12, 22, 11]))  # [11, 12, 22, 25, 64]
    print(solution.selectionSort([5, 1, 4, 2, 8]))       # [1, 2, 4, 5, 8]
    print(solution.selectionSort([]))                    # []
