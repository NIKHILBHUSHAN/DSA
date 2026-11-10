class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        """str=s.split()
        return len(str[-1])

        n=len(s)
        count=0
        last=0
        for i in range(n):
            if s[i]!=" ":
                count+=1
            elif count>0:
                last=count
                count=0
        return count if count>0 else last
        """
        
        i=len(s)-1
        count=0
        while i>=0 and s[i]==" ":
            i-=1
        while i>=0 and s[i]!=" ":
            count+=1
            i-=1
        return count
        