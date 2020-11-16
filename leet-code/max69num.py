class Solution:
    def maximum69Number (self, num: int) -> int:
        def change(s, index):
            S = list(s)
            S[index] = "6" if S[index] == "9" else "9"
            
            return int("".join(S))
        
        max = num
        s = str(num)
        for i in range(len(s)):
            if ( change(s, i) > max ):
                max = change(s, i)
            
        return max