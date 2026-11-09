class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        """for i in range(97,123):
            isfound=False
            for ch in sentence:
                if ord(ch)==i:
                    isfound=True
                    break
            if not isfound:
                return False
        return True"""
        alphabet=set()
        for ch in sentence:
            if ch not in alphabet:
                alphabet.add(ch)
        return len(alphabet)==26

        