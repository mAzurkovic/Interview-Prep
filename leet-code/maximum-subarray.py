def maxSubArray(nums) -> int:
    max_sum = nums[0]
    current_sum = 0
    for i in range(len(nums)):
        current_sum += nums[i]
        if nums[i] > current_sum:
            current_sum = nums[i]
        max_sum = max(max_sum, current_sum)

    return max_sum 







    # max_sum = nums[0]
    # current_sum = 0
    # i = 0
    # while i < len(nums):
    #     current_sum += nums[i]
    #     if (nums[i] > current_sum):
    #         current_sum = nums[i]

    #     if (current_sum > max_sum):
    #         max_sum = current_sum
    #     i += 1
    # return max_sum


print(maxSubArray([-2,2,5,-11,6]))