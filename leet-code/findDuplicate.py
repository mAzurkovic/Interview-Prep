def containsDuplicate(nums) -> bool:
    myDict = {}

    for i in nums:
        if (i not in myDict):
            myDict[i] = 1
        else:
            myDict[i] += 1
    
    for i in nums:
        if (myDict[i] >= 2):
            return True
        
    return False

    print(myDict)


print(containsDuplicate([0]))