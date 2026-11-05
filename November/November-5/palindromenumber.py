class Solution:
    def isPalindrome(self, x: int) -> bool:
        """s=str(x)
        reverse=""
        for i in range(len(s)-1,-1,-1):
            reverse+=s[i]
        return s==reverse"""
        if x<0:
            return False
        original=x
        reverse=0
        while x>0:
            last=x%10
            reverse=reverse*10+last
            x=x//10
        return original==reverse
        

        