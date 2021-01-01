    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        good = set()
        for i in allowed:
            if i not in good:
                good.add(i)
                
        num = len(words)
        for word in words:
            for char in word:
                if char not in good:
                    num -= 1
                    break
        return num