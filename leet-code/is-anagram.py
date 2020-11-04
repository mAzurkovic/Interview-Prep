def isAnagram(s, t) -> bool:
    myDict = {}

    for i in s:
        if (i not in myDict):
            myDict[i] = 1
        else:
            myDict[i] += 1
    
    for i in t:
        if (i not in myDict):
            return False
        else:
            myDict[i] -= 1
        
    for key in myDict:
        if (myDict[key] != 0):
            return False

    return True


print(isAnagram(" ", ""))
