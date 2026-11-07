class Solution:
    def validPalindrome(self, s: str) -> bool:
        def check(s:str):
            left=0
            right=len(s)-1
            while left<=right:
                if s[left]!=s[right]:
                    return False
                left+=1
                right-=1
            return True
        """if check(s):
            return True
        for i in range(len(s)):
            new=""
            for j in range(len(s)):
                if i!=j:
                    new+=s[j]
            if check(new):
                return True
        return False"""
        left=0
        right=len(s)-1
        while left<right:
            if s[left]!=s[right]:
                return check(left+1,right) or check(left,right-1)
            left+=1
            right-=1
        return True