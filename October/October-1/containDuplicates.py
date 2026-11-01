class Solution:
    def contains_Duplicate (self, nums: list[int]) -> bool:
        visited=set()
        for i in range(len(nums)):
            if nums[i] in visited:
                return True
            visited[nums[i]]=i
        return False