class NumArray:
    def __init__(self, nums: list[int]):
        self.prefix=[]
        totalsum=0
        for num in nums:
            totalsum+=num
            self.prefix.append(totalsum)

    def sumRange(self, left: int, right: int) -> int:
        if left==0:
            return self.prefix[right]
        return self.prefix[right]-self.prefix[left-1]