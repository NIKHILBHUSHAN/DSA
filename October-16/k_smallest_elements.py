"""
LeetCode-style Problem: Find K Smallest Elements Using Selection

Return the k smallest values in ascending order.
Use selection-sort logic manually; do not use sort(), sorted(), min(), or imports.
The original input list is left unchanged.
"""


class Solution:
    def kSmallest(self, nums: list, k: int) -> list:
        n = len(nums)

        if k < 0 or k > n:
            return []

        # Copy manually using append().
        values = []
        for value in nums:
            values.append(value)

        # The first k selection-sort passes place the k smallest values first.
        for i in range(k):
            smallest_index = i

            for j in range(i + 1, n):
                if values[j] < values[smallest_index]:
                    smallest_index = j

            if smallest_index != i:
                temp = values[i]
                values[i] = values[smallest_index]
                values[smallest_index] = temp

        result = []
        for i in range(k):
            result.append(values[i])

        return result


if __name__ == "__main__":
    solution = Solution()
    print(solution.kSmallest([7, 10, 4, 3, 20, 15], 3))  # [3, 4, 7]
    print(solution.kSmallest([1, 2, 3], 2))              # [1, 2]
    print(solution.kSmallest([5, 4], 0))                 # []
