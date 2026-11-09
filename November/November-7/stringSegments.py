class Solution:
    def countSegments(self, s: str) -> int:
        """segments=[]
        left=0
        right=0
        while right<len(s):
            if s[right]==" ":
                right+=1
                left=right
            else:
                left=right
                while right<len(s) and s[right]!=" ":
                    right+=1
                segemnt=""
                for i in range(left,right):
                    segemnt+=s[i]
                segments.append(segemnt)
        return len(segments)"""


        count=0
        left=0
        right=0
        while right<len(s):
            if s[right]!=" ":
                if right==0 or s[right-1]==" ":
                    count+=1
            right+=1
        return count

           


        