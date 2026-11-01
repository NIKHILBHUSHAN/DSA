class Solution:
    def longestOnes(self, nums: list[int], k: int) -> int:
        left = 0
        zero_count = 0
        max_length = 0

        for right in range(len(nums)):
            if nums[right] == 0:
                zero_count += 1

            if zero_count > k:
                if nums[left] == 0:
                    zero_count -= 1
                left += 1

            window_length = right - left + 1
            if window_length > max_length:
                max_length = window_length

        return max_length


if __name__ == "__main__":
    solution = Solution()
    print(solution.longestOnes([1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0], 2))  # 6
    print(solution.longestOnes([0, 0, 1, 1, 1, 0, 0], 0))              # 3
