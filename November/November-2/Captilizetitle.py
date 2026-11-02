class Solution:
    def capitalizeTitle(self, title: str) -> str:
        """words=title.split()
        captialize=[]
        for word in words:
            new=""
            if len(word)<=2:
                for char in word:
                    if 65<=ord(char)<=90:
                        new+=chr(ord(char)+32)
                    else:
                        new+=char
            else:
                for i in range(len(word)):
                    asc=ord(word[i])
                    if i==0:
                        if 97<=asc<=122:
                            new+=chr(asc-32)
                        else:
                            new+=word[i]
                    else:
                        if 65<=asc<=90:
                            new+=chr(asc+32)
                        else:
                            new+=word[i]
            captialize.append(new)
        return " ".join(captialize)"""
        words=title.split()
        result=[]
        for word in words:
            new=[]
            for i in range(len(word)):
                asc=ord(word[i])
                if len(word)<=2 or i>0:
                    if 65<=asc<=90:
                        asc+=32
                else:
                    if 97<=asc<=122:
                        asc-=32
                new.append(chr(asc))
            result.append("".join(new))
        return " ".join(result)




        