def firstUniqChar(s) -> int:
    charFreq = {}

    for i in s:
        if (i not in charFreq):
            charFreq[i] = 1
        else:
            charFreq[i] += 1

    for i in range(len(s)):
        char = s[i]
        if (charFreq[char] == 1):
            return i

    return -1

print(firstUniqChar(" qsqsqsqs"))