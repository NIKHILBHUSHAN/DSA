
class Solution:
    def rotateString(self, s: str, k: int) -> str:
        """
        n=len(s)
        if n==0:
            return s
        k=k%n
        for _ in range(k):
            last=s[n-1]
            temp=""
            temp+=last
            for i in range(n-1):
                temp+=s[i]
            s=temp
        return s
        """
        n=len(s)
        if n==0:
            return s
        k=k%n
        arr=[]
        for ch in s:
            arr.append(ch)
        i=0
        j=n-1
        while i<j:
            arr[i],arr[j]=arr[j],arr[i]
            i+=1
            j-=1
        i=0
        j=k-1
        while i<j:
            arr[i],arr[j]=arr[j],arr[i]
            i+=1
            j-=1
        i=k
        j=n-1
        while i<j:
            arr[i],arr[j]=arr[j],arr[i]
            i+=1
            j-=1
        result=""
        for ch in arr:
            result+=ch
        return result
