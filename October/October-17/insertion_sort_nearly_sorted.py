class Solution:
    def sortNearlySorted(self, nums):
        i = 1

        while i < len(nums):
            key = nums[i]
            j = i - 1

            while j >= 0 and nums[j] > key:
                nums[j + 1] = nums[j]
                j -= 1

            nums[j + 1] = key
            i += 1

        return nums


if __name__ == "__main__":
    nums = [2, 1, 3, 5, 4, 6]
    print(Solution().sortNearlySorted(nums))  # [1, 2, 3, 4, 5, 6]
