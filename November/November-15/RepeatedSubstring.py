class Solution:
    def repeatedSubstringPattern(self,s:str)->bool:
        """
        n=len(s)
        for length in range(1,n):
            if n%length==0:
                pattern=s[:length]
                repeated=""
                for i in range(n//length):
                    repeated+=pattern
                if repeated==s:
                    return True
        return False
        """
        n=len(s)
        for length in range(1,n//2+1):
            if n%length!=0:
                continue
            i=0
            j=length
            while j<n and s[i]==s[j]:
                i+=1
                j+=1
                if i==length:
                    i=0
            if j==n and i==0:
                return True
        return False