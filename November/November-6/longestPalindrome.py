class Solution:
    def longestPalindrome(self, s: str) -> int:
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
                if middle<value: 
                    longest-=middle
                    longest+=value
                    middle=value
        return longest

        
        
        