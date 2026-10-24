class Solution:
    def bubbleSort(self, nums: list[int]) -> list[int]:
        n = len(nums)

        for i in range(n):
            swapped = False

            for j in range(0, n - i - 1):
                if nums[j] > nums[j + 1]:
                    temp = nums[j]
                    nums[j] = nums[j + 1]
                    nums[j + 1] = temp
                    swapped = True

            if not swapped:
                break

        return nums


# Example:
# solution = Solution()
# print(solution.bubbleSort([1, 2, 3, 5, 4]))  # [1, 2, 3, 4, 5]
