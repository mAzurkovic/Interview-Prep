def recReverse(s, left, right):
    if (left > right):
        return s
    else:
        left += 1
        right -= 1
        return recReverse(s[left:right], left, right)

def reverseString(s) -> None:
    recReverse(s, 0, len(s) - 1)
    # left = 0
    # right = len(s) - 1

    # while (right > left):
    #     tmp = s[left]
    #     s[left] = s[right]
    #     s[right] = tmp

    #     left += 1
    #     right -= 1
    
    print(s)

reverseString(["h","e","l","l","o"])
