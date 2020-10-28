def searchInsert(nums, target) -> int:
    previous = 0
    index = 0
    if (target > nums[-1]):
        index = len(nums)

    for num in nums:
        if (num == target):
            index = nums.index(num)
        
        if ( (previous < target) and (target < num) ):
            index = nums.index(num)

        previous = num

    print(index)

searchInsert([1], 2)