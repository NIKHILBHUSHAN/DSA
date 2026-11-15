class Solution:
    def strStr(self,haystack:str,needle:str)->int:
        """
        for i in range(len(haystack)-len(needle)+1):
            j=0
            while j<len(needle) and haystack[i+j]==needle[j]:
                j+=1
            if j==len(needle):
                return i
        return -1
        """
        n=len(haystack)
        m=len(needle)
        if m==0:
            return 0
        if m>n:
            return -1
        for i in range(n-m+1):
            j=0
            while j<m and haystack[i+j]==needle[j]:
                j+=1
            if j==m:
                return i
        return -1