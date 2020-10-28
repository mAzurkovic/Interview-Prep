def climbStairs(n) -> int:
    if (n > 1):
        return climbStairs(n - 1) + climbStairs(n - 2) 
    else:
        return 1

print(climbStairs(38))