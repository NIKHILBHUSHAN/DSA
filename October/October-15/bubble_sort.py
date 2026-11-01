class Solution:
    def bubbleSort(self, nums: list[int]) -> list[int]:
        n = len(nums)

        for i in range(n):
            for j in range(0, n - i - 1):
                if nums[j] > nums[j + 1]:
                    temp = nums[j]
                    nums[j] = nums[j + 1]
                    nums[j + 1] = temp

        return nums


# Example:
# solution = Solution()
# print(solution.bubbleSort([5, 1, 4, 2, 8]))  # [1, 2, 4, 5, 8]
