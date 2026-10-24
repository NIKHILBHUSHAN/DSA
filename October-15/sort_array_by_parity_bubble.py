class Solution:
    def sortArrayByParity(self, nums: list[int]) -> list[int]:
        n = len(nums)

        for i in range(n):
            for j in range(0, n - i - 1):
                left_is_odd = nums[j] % 2 != 0
                right_is_even = nums[j + 1] % 2 == 0

                # Swap only when an odd number appears immediately before an even.
                if left_is_odd and right_is_even:
                    temp = nums[j]
                    nums[j] = nums[j + 1]
                    nums[j + 1] = temp

        return nums


# Example:
# solution = Solution()
# print(solution.sortArrayByParity([3, 1, 2, 4]))  # [2, 4, 3, 1]
