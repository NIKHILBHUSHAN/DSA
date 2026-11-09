class Solution:
    def longestPalindrome(self, s: str) -> int:
        """longest=0
        visited=[]
        middle=0
        for i in range(len(s)):
            if s[i] not in visited:
                count=0
                for j in range(len(s)):
                    if s[i]==s[j]:
                        count+=1
                visited.append(s[i])
                if count%2==0:
                    longest+=count
                else:
                    longest+=count-1
                    middle=1
        return longest+middle"""

        longest=0
        freq={}
        middle=0
        for ch in s:
            if ch not in freq:
                freq[ch]=1
            else:
                freq[ch]+=1
        for value in freq.values():
            if value%2==0:
                longest+=value
            else:
                longest+=value-1
                middle=1
        return longest+middle

        
        
        