class Solution:
    def countInversions(self, nums: list[int]) -> int:
        def merge_sort_count(arr: list[int]) -> tuple[list[int], int]:
            if len(arr) <= 1:
                return arr, 0

            mid = len(arr) // 2
            left, left_count = merge_sort_count(arr[:mid])
            right, right_count = merge_sort_count(arr[mid:])

            merged = []
            i = 0
            j = 0
            split_count = 0

            while i < len(left) and j < len(right):
                if left[i] <= right[j]:
                    merged.append(left[i])
                    i += 1
                else:
                    # Every remaining element in left is greater than right[j].
                    merged.append(right[j])
                    split_count += len(left) - i
                    j += 1

            while i < len(left):
                merged.append(left[i])
                i += 1

            while j < len(right):
                merged.append(right[j])
                j += 1

            total_count = left_count + right_count + split_count
            return merged, total_count

        _, inversion_count = merge_sort_count(nums)
        return inversion_count
