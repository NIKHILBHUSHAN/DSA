class Solution:
    def countSubstrings(self,s):
        '''
        n=len(s)
        count=0
        for i in range(n):
            for j in range(i,n):
                left=i
                right=j
                valid=True
                while left<right:
                    if s[left]!=s[right]:
                        valid=False
                        break
                    left+=1
                    right-=1
                if valid:
                    count+=1
        return count
        '''
        n=len(s)
        count=0
        for i in range(n):
            left=i
            right=i
            while left>=0 and right<n and s[left]==s[right]:
                count+=1
                left-=1
                right+=1
            left=i
            right=i+1
            while left>=0 and right<n and s[left]==s[right]:
                count+=1
                left-=1
                right+=1
        return count