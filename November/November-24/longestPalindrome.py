class Solution:
    def longestPalindrome(self,s):
        '''
        n=len(s)
        longest=""
        for i in range(n):
            for j in range(i,n):
                sub=s[i:j+1]
                left=0
                right=len(sub)-1
                valid=True
                while left<right:
                    if sub[left]!=sub[right]:
                        valid=False
                        break
                    left+=1
                    right-=1
                if valid and len(sub)>len(longest):
                    longest=sub
        return longest
        '''
        n=len(s)
        start=0
        end=0
        for i in range(n):
            left=i
            right=i
            while left>=0 and right<n and s[left]==s[right]:
                if right-left>end-start:
                    start=left
                    end=right
                left-=1
                right+=1
            left=i
            right=i+1
            while left>=0 and right<n and s[left]==s[right]:
                if right-left>end-start:
                    start=left
                    end=right
                left-=1
                right+=1
        return s[start:end+1]