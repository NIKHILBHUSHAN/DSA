class Solution:
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
        """unique=set()
        combine=nums1+nums2
        for num in combine:
            if num in nums1 and num in nums2:
                unique.add(num)
        return list(unique)"""
        nums1_unique=set(nums1)
        result=set()
        for num in nums2:
            if num in nums1_unique:
                result.add(num)
        return list(result)
        