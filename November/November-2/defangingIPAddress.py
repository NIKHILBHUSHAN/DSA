class Solution:
    def defangIPaddr(self, address: str) -> str:
        """block=address.split(".")
        return "[.]".join(block)"""
        result=[]
        for i in address:
            if i=='.':
                result.append("[.]")
            else:
                result.append(i)
        return "".join(result)
        