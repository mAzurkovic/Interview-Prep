def merge(nums1, m, nums2, n) -> None:
    j = 0

    if (len(nums2) > 0):
        for i in range(0, m):
            if nums2[j] < nums1[i]:
                tmp = nums1[i]
                nums1[i] = nums2[j]
                nums2[j] = tmp
                j += 1

        for i in range(0, n):
            nums1[m+i] = nums2[i]

    print(nums1)
    print(nums2)


merge([4,0,0,0,0,0], 1, [1,2,3,5,6], 5)
