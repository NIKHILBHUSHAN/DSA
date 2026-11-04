class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        """count=0
        for jewel in jewels:
            for stone in stones:
                if jewel==stone:
                    count+=1
        return count"""
        """count=0
        jewel=[ch for ch in jewels]
        for stone in stones:
            if stone in jewel:
                count+=1
        return count"""
        count=0
        jewel=set()
        for j in jewels:
            jewel.add(j)
        for stone in stones:
            if stone in jewel:
                count+=1
        return count
                