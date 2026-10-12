class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        freq = {}
        for num in nums:
            if num in freq:
                freq[num]+=1
            else:
                freq[num]=1
        for num in nums:
            if freq[num]==1:
                return num
        return -1

        