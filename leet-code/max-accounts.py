class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        max = 0
        for i in accounts:
            currentSum = sum(i)
            max = max if max > currentSum else currentSum
            
        return max
    