class Solution:
    def reorganizeString(self,s):
        '''
        def generate(arr,pos):
            if pos==len(arr):
                valid=True
                for i in range(1,len(arr)):
                    if arr[i]==arr[i-1]:
                        valid=False
                        break
                if valid:
                    return "".join(arr)
                return ""
            for i in range(pos,len(arr)):
                arr[pos],arr[i]=arr[i],arr[pos]
                result=generate(arr,pos+1)
                if result!="":
                    return result
                arr[pos],arr[i]=arr[i],arr[pos]
            return ""
        return generate(list(s),0)
        '''
        n=len(s)
        freq={}
        for ch in s:
            if ch not in freq:
                freq[ch]=1
            else:
                freq[ch]+=1
        most=""
        highest=0
        for ch in freq:
            if freq[ch]>highest:
                highest=freq[ch]
                most=ch
        if highest>(n+1)//2:
            return ""
        res=[""]*n
        index=0
        for ch in freq:
            if ch==most:
                continue
            for i in range(freq[ch]):
                if index>=n:
                    index=1
                res[index]=ch
                index+=2
        for i in range(0,n,2):
            res[i]=most
            if i//2+1==highest:
                break
        return "".join(res)