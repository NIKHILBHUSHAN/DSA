class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        visited={}
        for i in range(len(nums)):
            need=target-nums[i]
            if need in visited:
                return [visited[need], i]
            visited[nums[i]]=i
        return [-1,-1]