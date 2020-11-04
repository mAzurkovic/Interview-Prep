def reverseWords(s) -> str:
    sReturn = ""
    words = s.split()
    
    left = 0
    right = len(words) - 1

    while (right > left):
        tmp = words[left]
        words[left] = words[right]
        words[right] = tmp

        left += 1
        right -= 1
    
    for i in words:
        sReturn = sReturn + i + " "

    print(sReturn[0:len(sReturn) - 1])

reverseWords("     the sky is blue    ")