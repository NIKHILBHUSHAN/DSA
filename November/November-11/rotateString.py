
class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        """

        if len(s)!=len(goal):
            return False
        temp=s
        for i in range(len(s)):
            if temp==goal:
                return True
            temp=temp[1:]+temp[0]
        return False
        """

         
        n=len(s)
        if n!=len(goal):
            return False

        for i in range(n):
            j=0
            while j<n and s[(i+j)%n]==goal[j]:
                j+=1
            if j==n:
                return True

        return False
