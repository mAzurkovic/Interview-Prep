def findDuplicate(nums) -> int:
    tort = hare = 0
    while True:
        tort = nums[tort]
        hare = nums[nums[hare]]
        if (tort == hare):
            break
    
    for i in nums:
        if i == nums[hare]:
            return i
        hare -= 1
        
    return -1


    # seen = set()
        
    # for i in nums:
    #     if i in seen:
    #         return i
    #     else:
    #         seen.add(i)

print(findDuplicate([1,2,3,4,5,6,3]))