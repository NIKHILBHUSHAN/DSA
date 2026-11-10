class Solution:
    def shortestToChar(self, s: str, c: str) -> list[int]:
        """indices=[]
        distance=[]
        for i in range(len(s)):
            if s[i]==c:
                indices.append(i)
        for i in range(len(s)):
            mindist=len(s)
            for j in indices:
                mindist=min(mindist,abs(i-j))
            distance.append(mindist)
        return distance"""
        distance=[0]*len(s)
        prev=-len(s)
        for i in range(len(s)):
            if s[i]==c:
                prev=i
            distance[i]=i-prev
        prev=2*len(s)
        for i in range(len(s)-1,-1,-1):
            if s[i]==c:
                prev=i
            distance[i]=min(distance[i],prev-i)
        return distance

            
                
        