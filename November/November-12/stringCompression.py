class Solution:
    def compress(self, chars: list[str]) -> int:
        """comp=[]
        i=0
        while i<len(chars):
            ch=chars[i]
            count=1
            j=i+1
            while j<len(chars) and chars[j]==ch:
                count+=1 
                j+=1
            comp.append(ch)
            if count>1:
                for digit in str(count):
                    comp.append(digit)
            i=j
        for i in range(len(comp)):
            chars[i]=comp[i]
        return len(comp)"""
        read=0
        write=0
        n=len(chars)
        while read<n:
            count=0
            ch=chars[read]
            while read<n and chars[read]==ch:
                count+=1
                read+=1
            chars[write]=ch
            write+=1
            if count>1:
                for digit in str(count):
                    chars[write]=digit
                    write+=1
        return write        
        