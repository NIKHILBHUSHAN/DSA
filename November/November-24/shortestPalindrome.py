class Solution:
    def shortestPalindrome(self,s):
        '''
        n=len(s)
        longest=0
        for i in range(n,0,-1):
            left=0
            right=i-1
            valid=True
            while left<right:
                if s[left]!=s[right]:
                    valid=False
                    break
                left+=1
                right-=1
            if valid:
                longest=i
                break
        result=""
        i=n-1
        while i>=longest:
            result+=s[i]
            i-=1
        return result+s
        '''
        n=len(s)
        longest=0
        for i in range(n,0,-1):
            left=0
            right=i-1
            valid=True
            while left<right:
                if s[left]!=s[right]:
                    valid=False
                    break
                left+=1
                right-=1
            if valid:
                longest=i
                break
        prefix=""
        i=n-1
        while i>=longest:
            prefix+=s[i]
            i-=1
        return prefix+s