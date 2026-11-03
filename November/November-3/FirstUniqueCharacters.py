class Solution:
    def firstUniqChar(self, s: str) -> int:
        """for i in range(len(s)):
            count=0
            for j in range(len(s)):
                if s[i]==s[j]:
                    count+=1
            if count==1:
                return i
        return -1"""
        
        freq={}
        for char in s:
            if char not in freq:
                freq[char]=1
            else:
                freq[char]+=1
        for i in range(len(s)):
            if freq[s[i]]==1:
                return i
        return -1
        