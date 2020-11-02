def rotate(nums, k):
    if (k > len(nums)):
        k = k % len(nums)



    end = nums[0:len(nums) - k]
    start = nums[len(nums) - k:]
    nums[:] = start + end

    print(nums)



rotate( [1,2], 3)