def makeDict(arr):
    myDict = {}
    for i in arr:
        if (i not in myDict):
            myDict[i] = 1
        else:
            myDict[i] += 1
        
    return myDict

def intersect(nums1, nums2):
    dict1 = makeDict(nums1)
    dict2 = makeDict(nums2)
    arr1 = []

    if (len(nums2) <= len(nums1)):
        for i in dict2:
            if (i in dict1):
                for j in range(0, min(dict2[i], dict1[i])):
                    arr1.append(i)
        
        return arr1
    else: 
        for i in dict1:
            if (i in dict2):
                for j in range(0, min(dict2[i], dict1[i])):
                    arr1.append(i)
        return arr1 

    return []




print(intersect([1,2,2], [1,2,2,1]))
